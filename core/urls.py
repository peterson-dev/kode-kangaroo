from django.urls import path
from . import views 
from core.views import FolderDetailView, SnippetDetailView

urlpatterns = [
    # path('', views.HomePageView.as_view(model=UserPost), name='index'),
    path('snippets/<slug:slug>/', views.SnippetDetailView.as_view(), name='snippet-detail'),
    path('folders/<int:pk>/', views.FolderDetailView.as_view(), name='folder-detail'),
]
