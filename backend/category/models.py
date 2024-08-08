import json
from django.db import models
from problems.models import Problem

class Category(models.Model):
    name = models.CharField(max_length=100)
    num_problems = models.IntegerField()

    def __str__(self):
        return self.name

    def list_all_problems(self, category_name):
        problems = Problem.objects.filter(category=category_name)
        problem_list = [
            {
                'title': problem.title,
                'description': problem.description,
                'category': problem.category,
                'difficulty': problem.difficulty,
                'link': problem.link
            }
            for problem in problems
        ]
        return problem_list

    def list_all_category(self):
        categories = Category.objects.all()
        category_list = [
            {
                'name': theCategory.name,
                'num_problems': theCategory.num_problems
            }
            for theCategory in categories
        ]
        return category_list