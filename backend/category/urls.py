from django.urls import path
from .paths import list_all_categories, list_all_problems

urlpatterns = [
    path('category/all/', list_all_categories, name='list_all_categories'),
    path('category/problems/', list_all_problems, name='list_all_problems'),
]