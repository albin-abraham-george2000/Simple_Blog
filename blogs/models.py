from django.db import models
from auth_users.models import Users
from django.conf import settings
from django.utils.text import slugify


# Create your models here.


class BlogPostFilterManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(blog_Status='published').order_by('blog_created_at')

class UserBlogManaer(models.Manager):
    def for_user(self,user):
        return super().get_queryset().filter(blog_Author=user)
    
class Blog(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived')
    )
   
    blog_Title = models.CharField(max_length=50)
    blog_Desc = models.TextField()
    blog_Status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    blog_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_created_at = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()
    published = BlogPostFilterManger()
    user_post = UserBlogManaer()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_Title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.blog_Title
    class Meta:
        ordering =['-blog_created_at']
        verbose_name = 'Blog_Post'
        verbose_name_plural = 'Blog Posts'
    
    