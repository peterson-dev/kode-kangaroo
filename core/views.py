from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Folder, Snippet
from .forms import NewSnippetForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


# from django.shortcuts import redirect, render

class SnippetListView(LoginRequiredMixin, ListView):
    model = Snippet
    context_object_name = 'snippets'
    template_name = 'core/snippet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewSnippetForm
        return context

@require_http_methods(['POST'])
@login_required
def new_snippet(request):
    # if request.content_type == 'application/json':
    #     body = json.loads(request.body)
    # else:
    #     body = request.POST
    
    form = NewSnippetForm(request.POST)

    if form.is_valid():
        form.save(user=request.user)

        # if request.is_ajax():
        #     return render(request, 'partials/snippets.html', {'snippet': snippet})

    return redirect('snippet_list')

class FolderDetailView(LoginRequiredMixin, DetailView):
    model = Folder
    template_name = 'core/folder_contents.html'

class SnippetDetailView(LoginRequiredMixin, DetailView):
    model = Snippet
    template_name = 'core/snippet_detail.html'

class SnippetUpdateView(LoginRequiredMixin, UpdateView):
    model = Snippet
    template_name = 'core/update_snippet.html'
    fields = ['title', 'post_content', 'public']
    success_url = reverse_lazy('snippet_list')

class SnippetDeleteView(LoginRequiredMixin, DeleteView):
    model = Snippet
    template_name = 'core/confirm_snippet_delete.html'
    success_url = reverse_lazy('snippet_list')

    def form_validation(self, request):

        if self.request.is_ajax():
            return JsonResponse({"complete": True})

        return redirect('core/snippet_list.html')


def user_public_snippets(request, pk):
    template_name = 'core/user_public_detail.html'
    snippets = Snippet.objects.filter(public=True)
    print(snippets)

    context = {
        'snippets': snippets,
    }

    return render(request, 'core/user_public_detail.html', context)

def all_public_snippets(request):
    template_name = 'core/discover_list.html'
    snippets = Snippet.objects.filter(public=True)
    print(snippets)

    context = {
        'snippets': snippets,
    }

    return render(request, 'core/discover_list.html', context)


#
# # From class need to create APIView.  
# class SnippetDetail (APIView):
#     def delete (self, request, pk):
#         task = get_object_or_404()
