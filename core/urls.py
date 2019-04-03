from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('snippets/', views.SnippetListView.as_view(), name='snippet_list'),
    path('snippets/<slug:slug>/', views.SnippetDetailView.as_view(), name='snippet_detail'),
    path('folders/<int:pk>/', views.FolderDetailView.as_view(), name='folder-detail'),
]
