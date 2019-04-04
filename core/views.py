from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Folder, Snippet
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse

# from django.shortcuts import redirect, render

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

class SnippetUpdateView(LoginRequiredMixin, UpdateView):
    model = Snippet
    template_name = 'core/update_snippet.html'
    fields = ['title', 'post_content', 'languages']
    success_url = reverse_lazy('snippet_list')

class SnippetDeleteView(LoginRequiredMixin, DeleteView):
    model = Snippet
    template_name = 'core/confirm_snippet_delete.html'
    success_url = reverse_lazy('snippet_list')

    def form_validation(self, request):

        if self.request.is_ajax():
            return JsonResponse({"complete": True})

        return redirect('core/snippet_list.html')
#
# # From class need to create APIView.  
# class SnippetDetail (APIView):
#     def delete (self, request, pk):
#         task = get_object_or_404()

