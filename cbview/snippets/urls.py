from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetsView.as_view()),
    path('snippet/<int:pk>/', views.SnippetView.as_view()),
    path('users/', views.UsersView.as_view()),
    path('user/<int:pk>/', views.UserView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)