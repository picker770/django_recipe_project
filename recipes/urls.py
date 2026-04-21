from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='detail'),
    path('create/', views.recipe_create, name='create'),
    path('update/<int:pk>/', views.recipe_update, name='update'),
    path('delete/<int:pk>/', views.recipe_delete, name='delete'),
]