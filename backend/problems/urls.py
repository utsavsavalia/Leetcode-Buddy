# leetcode_buddy/problems/urls.py
# problems/urls.py
from django.urls import path
from .paths import problem_of_the_day

urlpatterns = [
    path('problem_of_the_day/', problem_of_the_day, name='problem_of_the_day'),
    # Add more URLs specific to the 'problems' app if needed
]