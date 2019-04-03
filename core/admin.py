from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Snippet, Language, Folder

# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'post_content', 'source_id')
    exclude = ('slug',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder')

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('title')
    exclude = ('category')

