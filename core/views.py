from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Folder, Snippet

class FolderDetailView(LoginRequiredMixin, DetailView):
    model = Folder
    template_name = 'core/folder_contents.html'

class SnippetDetailView(LoginRequiredMixin, DetailView):
    model = Snippet

