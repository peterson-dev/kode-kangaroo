from django.urls import path
from . import views 

urlpatterns = [
    path('snippets/', views.SnippetListView.as_view(), name='snippet_list'),
    path('snippets/new/', views.new_snippet, name='new-snippet'),
    path('snippets/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippet/<int:pk>/', views.SnippetUpdateView.as_view(), name='snippet-update'),
    path('folders/<int:pk>/', views.FolderDetailView.as_view(), name='folder-contents'),
    path('snippet/<int:pk>/delete', views.SnippetDeleteView.as_view(), name='confirm-snippet-delete'),
    path('snippets/user/<int:pk>', views.user_public_snippets, name = 'user_snippets'),
    path('snippets/kommunity', views.all_public_snippets, name = 'kommunity_list'),
    path('snippet/<int:pk>/copy', views.SnippetCopyView.as_view(), name='copy-snippet'),
]
