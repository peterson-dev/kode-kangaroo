from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Folder, Snippet
# from django.shortcuts import redirect, render


# def index(request):
#     if request.user.is_authenticated:
#         return redirect('snippet_list')

#     return render(request, "registration/login.html")

class SnippetListView(LoginRequiredMixin, ListView):
    model = Snippet
    context_object_name = 'snippets'
    template_name = 'core/snippet_list.html'

class FolderDetailView(LoginRequiredMixin, DetailView):
    model = Folder
    template_name = 'core/folder_contents.html'

class SnippetDetailView(LoginRequiredMixin, DetailView):
    model = Snippet
    template_name = 'core/snippet_detail.html'

