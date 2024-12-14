from django.shortcuts import render,get_object_or_404,reverse
from meal.models import Meal
from .forms import ReservationForm
from .models import Reservation
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def reservation_list(request):
    reservations = Reservation.objects.filter(customer=request.user).order_by("-created_on")
    return render(
        request,
        'reservation/reservation_list.html',
        {'reservations':reservations}
    )

def reservation(request):

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.customer = request.user
            reservation_form.save()
            messages.add_message(request, messages.SUCCESS, 'Reservation added')
            return HttpResponseRedirect(reverse('reservation_list'))
        else:
            messages.add_message(request, messages.ERROR, 'Error happened')
    reservation_form = ReservationForm()
    # paginate_by = 6
    return render(
        request,
        "reservation/reserve.html",
        {'reservation_form':reservation_form}
    )

def delete_reservation(request, reservation_id):
    """
    view to delete Reservation
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    print('reservation deleted')


    return HttpResponseRedirect(reverse('reservation_list'))

def delete_reservations(request):
    """
    view to delete Reservation
    """
    reservations = Reservation.objects.all()
    for reservation in reservations:           
        reservation.delete()
    print('reservation deleted')


    return HttpResponseRedirect(reverse('reservation_list'))