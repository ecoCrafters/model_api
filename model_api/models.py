from django.db import models
from django.contrib.auth.models import User

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class UploadImageTest(models.Model):
    label = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)