# Generated by Django 2.2 on 2019-04-02 18:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures')),
                ('slug', models.SlugField()),
                ('email', models.CharField(max_length=50)),
                ('gender_pronouns', models.CharField(blank=True, max_length=20, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('about', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_admin', models.BooleanField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('folder', models.ManyToManyField(to='core.Folder')),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('post_content', models.TextField(max_length=5000)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('source_id', models.CharField(max_length=10, null=True)),
                ('languages', models.ManyToManyField(to='core.Language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='folder',
            name='category',
            field=models.ManyToManyField(related_name='folder_category', to='core.Language'),
        ),
        migrations.AddField(
            model_name='folder',
            name='user',
            field=models.ManyToManyField(related_name='folder_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='folder',
            field=models.ManyToManyField(related_name='users_folder', to='core.Folder'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
