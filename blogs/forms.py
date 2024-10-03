from .models import Blog
from django import forms
from tinymce.widgets import TinyMCE


class BlogForm(forms.ModelForm):
        
    class Meta:
        model = Blog
        fields = ['blog_Title','blog_Desc','blog_Status']
        

        widgets = {
            'blog_Title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the title of the blog'
                }
            ),
            'blog_Desc': TinyMCE(),
            'blog_Status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
             ),
            }


# #################### FORM VALIDATION  ############################
