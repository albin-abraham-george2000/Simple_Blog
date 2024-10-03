from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/new_blog_list.html'
    context_object_name = 'blogs'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(blog_Status='published')
        return queryset
    
    

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Blog
    template_name = 'blogs/new_blog_detail.html'
    context_object_name = 'blog'
    slug_field ='slug'
    slug_url_kwarg = 'slug'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blogs/blog_form.html'
    fields = ['blog_Title', 'blog_Desc', 'blog_Status']
    success_url = reverse_lazy('Blogs:blog-list')

    def form_valid(self, form):
        form.instance.blog_Author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Blog'
        return context


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Blog
    template_name = 'blogs/blog_form.html'
    form_class = BlogForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = success_url = reverse_lazy('Blogs:blog-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.blog_Author = self.request.user
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm):
        return super().form_invalid(form)

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.blog_Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Blog'
        return context


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('Blogs:blog-list')

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.blog_Author

    