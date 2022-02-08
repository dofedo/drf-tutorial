from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippets),
    path('snippets/<int:pk>/', views.snippet),
]