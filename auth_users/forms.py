from auth_users.models import Users
from django import forms
from django.contrib.auth.forms import (
                                        UserChangeForm, 
                                        UserCreationForm, 
                                        AuthenticationForm
                                        )


class UserRegistrationForm(UserCreationForm):
    
    def __init__(self,*args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class':"bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                'placeholder':'Enter your username'
                })
        self.fields['email'].widget.attrs.update(
            {
                'class':"bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                'placeholder':'Enter the your email address'
                }
            )
        self.fields['password1'].widget.attrs.update(
            {
                'class':"bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                'placeholder':'Enter the your password'
                }
            )
        self.fields['password2'].widget.attrs.update(
            {
                'class':"bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                'placeholder':'Retye your password'
                }
            )
        self.fields['username'].error_messages = {
            'required': 'Username should be set'
        }
       
    class Meta:
        model = Users
        fields = ('email','username')
        
       
        
        
       
        

class UserLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class':"bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" ,
            'placeholder':'Enter your username '
        })
        
        self.fields['password'].widget.attrs.update({
            'class':"bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            'placeholder':'Enter your password '
        })
    


class UserUpdateForm(UserChangeForm):
    
    class Meta:
        model = Users
        fields = [ 'email', 'first_name', 'last_name']
        help_text = {
            'password' : None,
        }
        
class EmailValidationForm(forms.Form):
    email = forms.EmailField(label='Email Address')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not Users.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email address.")
        return email

            
        
    
     