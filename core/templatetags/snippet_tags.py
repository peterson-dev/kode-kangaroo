from django import template
from core.models import Snippet, User, Folder

register = template.Library()

@register.inclusion_tag('user_folders.html')
def show_user_folders(user):
    user_folders = Folder.objects.filter(user=user).order_by('-title')
    return {'user_folders': user_folders} 