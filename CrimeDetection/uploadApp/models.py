from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
def get_upload_path(instance, filename):
    return 'documents/{0}/{1}'.format(instance.user.username, filename)

class Document(models.Model):
    docfile = models.FileField(upload_to=get_upload_path)