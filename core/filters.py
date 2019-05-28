import django_filters
from core.models import Snippet, Folder, User

class SnippetFilter(django_filters.FilterSet):

    class Meta:
        model=Snippet
        # fields = ('title', 'content', 'language', 'user',)
        fields = {
            'title': ['icontains',], 
            'content': ['icontains',], 
            'language': ['exact',], 
            'user': ['exact',],
        }

class SnippetListFilter(django_filters.FilterSet):

    class Meta:
        model=Snippet
        # fields = ('title', 'content', 'language',)
        fields = {
            'title': ['icontains',], 
            'content': ['icontains',], 
            'language': ['exact',], 
        }