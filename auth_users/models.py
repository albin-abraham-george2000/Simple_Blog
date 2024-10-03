from django.db import models
from django.contrib.auth.models import AbstractUser
import os,re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError




# Create your models here.


class Users(AbstractUser):
    
    profile_pics = models.FileField(upload_to='profile_pics', null=True, blank=True)
    user_bio = models.CharField(max_length = 500 , blank= True)
    
    class Meta:
        verbose_name = "User Profile" 
        verbose_name_plural = "User Profiles"
    
    def save(self, *args, **kwargs):
        if self.pk:  
            old_profile = Users.objects.get(pk=self.pk)
            if old_profile.profile_pics and old_profile.profile_pics != self.profile_pics:
               
                if os.path.isfile(old_profile.profile_pics.path):
                    os.remove(old_profile.profile_pics.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
       
        if self.profile_pics and os.path.isfile(self.profile_pics.path):
            os.remove(self.profile_pics.path)
        super().delete(*args, **kwargs)

        
   