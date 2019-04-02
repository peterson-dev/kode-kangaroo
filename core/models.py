from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField

# Create your models here.

class User(AbstractUser):
    '''This model represents the custom user model'''
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    slug = AutoSlugField(populate_from='username', unique=True)
    email = models.CharField(max_length=50, null=False, blank=False)
    gender_pronouns = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    is_admin = models.BooleanField()
    is_active = models.BooleanField()

class Language(models.Model):
    '''This model represents the language category'''
    name = models.CharField(max_length=50)

class Snippet(models.Model):
    '''This model represents the users post'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    languages = models.ManyToManyField(Language)
    post_content = models.TextField(max_length=5000)
    slug = AutoSlugField(populate_from='title', unique=True)
    created_at = models.DateTimeField(auto_now=True)
    source_id = models.CharField(max_length=10, null=True)
