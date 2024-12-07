from django.shortcuts import render
from django.views import generic
from .models import Meal
# Create your views here.

class MealList(generic.ListView):
    queryset = Meal.objects.all()
    template_name = 'meal/meal_list.html'
    paginate_by = 6
