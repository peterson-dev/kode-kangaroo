from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Folder(models.Model):
    '''This model represents the folder model'''
    title = models.CharField(max_length=35, unique=True)
    user = models.ManyToManyField('User', related_name='user')
    snippets = models.ManyToManyField('Snippet', null=True, blank=True)

    def save(self, *args, **kwargs):
        for field_name in ['title']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(Folder, self).save(*args, **kwargs)

    def __str__(self):
        return self.title.upper()

class User(AbstractUser):
    '''This model represents the custom user model'''
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    slug = models.SlugField()
    email = models.CharField(max_length=50, null=False, blank=False)
    gender_pronouns = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    folder = models.ManyToManyField('Folder', related_name='users_folder', null=True, blank=True)

    def set_slug(self):
        '''Creates a unique slug for every post'''
        if self.slug:
            return
          
    def save(self, *args, **kwargs):
        '''Hides slug field in admin- saves slug to use in url'''
        self.set_slug()
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'slug': self.slug})

    def __str__(self):
        return self.username

class Snippet(models.Model):
    '''This model represents the users post'''
    LANG_CHOICES = (
   #('actual value for model', 'human-readable name')
    ('bash', 'Bash'),
    ('basic', 'Basic'),
    ('c', 'C'),
    ('css', 'CSS'),
    ('csharp', 'C#'),
    ('cpp', 'C++'),
    ('coffee', 'CoffeeScript'),
    ('clojure', 'Clojure'),
    ('docker', 'Docker'),
    ('elixir', 'Elixir'),
    ('fsharp', 'F#'),
    ('git', 'Git'),
    ('go', 'Go'),
    ('graphql', 'GraphQL'),
    ('html', 'HTML'),
    ('java', 'Java'),
    ('js', 'Javascript'),
    ('json', 'JSON'),
    ('monkey', 'Monkey'),
    ('objectivec', 'Objective-C'),
    ('pascal', 'Pascal'),
    ('perl', 'Perl'),
    ('php', 'PHP'),
    ('py', 'Python'),
    ('jsx', 'React JSX'),
    ('ruby', 'Ruby'),
    ('rust', 'Rust'),
    ('sql', 'SQL'),
    ('swift', 'Swift'),
    ('ts', 'typescript'),
    ('yml', 'YAML'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    language = models.CharField(max_length=420, choices=LANG_CHOICES)
    post_content = models.TextField(max_length=15000)
    created_at = models.DateTimeField(auto_now=True)
    source_id = models.CharField(max_length=10, null=True, blank=True)
    public=models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
    
    def get_absolute_url(self):
        return reverse("snippet-detail", args=[str(self.slug)])
    
    def __str__(self):
        return self.title
