
from .forms import UserUpdateForm , UserRegistrationForm, UserLoginForm
from .forms import EmailValidationForm
from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from blogs.models import Blog
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_list_or_404
from auth_users.models import Users



# Create your views here.

class Sampleview(TemplateView):
    template_name = 'users/blog.html'
    
    
    def get(self,request):
        return render(request,self.template_name)

class SampleProfileView(TemplateView):
    template_name = 'users/new_profile.html'
    
    
    def get(self,request):
        return render(request,self.template_name)


#   My lOGIC
class UserRegistrationView(TemplateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
           
            user_inst = form.save(commit=False)  
            password = form.cleaned_data['password1']  
            user_inst.set_password(password)
            user_inst.save()

            print(f'{user_inst.username} has been registered successfully')
            return redirect('auth_users:login')
        
        
        return self.render_to_response({'form': form})

class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'
    
    success_url = reverse_lazy('auth_users:user-profile')
    
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    


class UserProfileView(TemplateView):
    template_name = 'users/new_profile.html'
    form_class = UserUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['form'] = self.form_class(instance=self.request.user)  
        
        user = self.request.user
        context['user'] = user
        
        user_blogs = Blog.user_post.for_user(user)
        context['blogs_post'] = user_blogs.filter(blog_Status='published')
        context['blogs_draft'] = user_blogs.filter(blog_Status='draft')
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.request.user)
        if form.is_valid():
            form.save()
            return redirect('auth_users:user_profile')  
        
        
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    

class ForgotPasswordView(FormView):
    template_name = 'users/forgot_password.html'
    form_class = EmailValidationForm
    success_url = reverse_lazy('auth_users:reset-password')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = Users.objects.get(email=email)
        self.request.session['reset_user_id'] = user.id 
        return redirect(self.success_url)


class ResetPasswordView(FormView):
    template_name = 'users/reset_password.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('auth_users:login')

    def get_form(self, *args, **kwargs):
        user_id = self.request.session.get('reset_user_id')
        user = Users.objects.get(id=user_id)  
        return self.form_class(user=user, **self.get_form_kwargs())  
    
    def form_valid(self, form):
        form.save()  # Save the new password
        return super().form_valid(form)