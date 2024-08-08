from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Category
import json

@require_GET
def list_all_categories(request: HttpRequest):
    category_obj = Category()
    category_list = category_obj.list_all_category()
    return JsonResponse(category_list, safe=False)

@require_POST
def list_all_problems(request: HttpRequest):
    try:
        body = json.loads(request.body)
        category_name = body.get("category_name")

        if not category_name:
            return JsonResponse({"success": False, "error": "category_name is required"}, status=400)
        
        category_obj = Category()
        problem_list = category_obj.list_all_problems(category_name)
        return JsonResponse(problem_list, safe=False)

    except json.JSONDecodeError as e:
        return JsonResponse({"success": False, "error": "Invalid JSON format"}, status=400)