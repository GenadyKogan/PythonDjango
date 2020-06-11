from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
def get_upload_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default=0)

    
    docfile = models.FileField(upload_to=get_upload_path)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

