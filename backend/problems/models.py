import random
from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def problem_of_the_day(self):
        # Get the total count of problems
        total_problems = Problem.objects.count()
        
        # Generate a random index
        if total_problems == 0:
            return None

        random_index = random.randint(0, total_problems - 1)
        
        # Get the problem at that index
        problem = Problem.objects.all()[random_index]
        return problem