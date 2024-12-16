from django.shortcuts import render
from meal.models import Meal

# Create your views here.

def home_page(request):
    meal_list = Meal.objects.all()
    # paginate_by = 6
    return render(
        request,
        "home_page/home.html",
        {'meal_list':meal_list}
    )