# leetcode_buddy/problems/views.py
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET
from .models import Problem


@require_GET
def problem_of_the_day(request: HttpRequest):
    problem = Problem()
    problem = problem.problem_of_the_day()
    problem_data = {
        'title': problem.title,
        'description': problem.description,
        'category': problem.category,
        'difficulty': problem.difficulty,
        'link': problem.link,
    }
    return JsonResponse(problem_data)
