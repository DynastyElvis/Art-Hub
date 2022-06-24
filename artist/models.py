from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt



class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
        
    @classmethod  
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile
        
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    
    
class Comments(models.Model):
    comment = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def save_comment(self):
        self.save()
    
    def delete_comments(self):
        self.delete()
        
    @classmethod
    def get_comment_by_image(cls,id):
        comment = Comments.objects.filter(post__pk = id)
        return 