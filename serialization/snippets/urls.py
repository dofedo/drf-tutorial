from traceback import format_exception_only
from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.Snippets.as_view()),
    path('snippets/<int:pk>/', views.Snippet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)