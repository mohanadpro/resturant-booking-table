from django.shortcuts import render
from meal.models import Meal
from .forms import ReservationForm
from .models import Reservation
# Create your views here.
def reservation(request):
    reservations = Reservation.objects.all()
    for reservation in reservations:
        print(reservation.customer, reservation.table)

    meal_list = Meal.objects.all()
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            print('Reservation is saved successfully')
    reservation_form = ReservationForm()
    # paginate_by = 6
    return render(
        request,
        "reservation/reservation.html",
        {'meal_list':meal_list,'reservation_form':reservation_form}
    )
