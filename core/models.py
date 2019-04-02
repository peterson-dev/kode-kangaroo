from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Folder(models.Model):
    '''This model represents the folder model'''
    name = models.CharField(max_length=35)
    language = models.ManyToManyField(Language)
    user = models.ManyToManyField(User)


class User(AbstractUser):
    '''This model represents the custom user model'''
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    slug = models.SlugField()
    email = models.CharField(max_length=50, null=False, blank=False)
    gender_pronouns = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    is_admin = models.BooleanField()
    is_active = models.BooleanField()
    folder = models.ManyToManyField(Folder)


    def set_slug(self):
        '''Creates a unique slug for every post'''
        if self.slug:
            return
        base_slug = slugify(self.title)

        slug = base_slug
        n = 0

        while User.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + '-' + str(n)
        
        self.slug = slug
    
    def save(self, *args, **kwargs):
        '''Hides slug field in admin- saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("user_profile", args=[str(self.slug)])
    
    def __str__(self):
        return self.username


class Language(models.Model):
    '''This model represents the language category'''
    name = models.CharField(max_length=50)
    folder = models.ManyToManyField(Folder)

class Snippet(models.Model):
    '''This model represents the users post'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    languages = models.ManyToManyField(Language)
    post_content = models.TextField(max_length=5000)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now=True)
    source_id = models.CharField(max_length=10, null=True)

    def set_slug(self):
        '''Creates a unique slug for every post'''
        if self.slug:
            return
        base_slug = slugify(self.title)

        slug = base_slug
        n = 0

        while User.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + '-' + str(n)
        
        self.slug = slug
    
    def save(self, *args, **kwargs):
        '''Hides slug field in admin- saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("snippet_detail", args=[str(self.slug)])
    
    def __str__(self):
        return self.title


