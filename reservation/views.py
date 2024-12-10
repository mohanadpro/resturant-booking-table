from django.shortcuts import render
from meal.models import Meal
# Create your views here.
def reservation(request):
    meal_list = Meal.objects.all()
    paginate_by = 6
    return render(
        request,
        "reservation/reservation.html",
        {'meal_list':meal_list}
    )
