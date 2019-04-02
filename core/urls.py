from django.urls import path
from . import view, FolderDetailView, SnippetDetailView

urlpatterns = [
    # path('', views.HomePageView.as_view(model=UserPost), name='index'),
    path('snippets/<slug:slug>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('folders/<int:pk>/', FolderDetailView.as_view(), name='folder-detail'),
]
