from django.shortcuts import render,get_object_or_404,reverse
from meal.models import Meal
from .forms import ReservationForm
from .models import Reservation
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import date,datetime
# import 
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
        if reservation_form.is_valid() == False:
            messages.add_message(request, messages.ERROR, 'Error happened')
        elif datetime.strptime(reservation_form['date'].value(),'%Y-%m-%d') < datetime.strptime(datetime.utcnow().strftime('%Y-%m-%d'),'%Y-%m-%d') or (datetime.strptime(reservation_form['date'].value(),'%Y-%m-%d') == datetime.strptime(datetime.utcnow().strftime('%Y-%m-%d'),'%Y-%m-%d') and (datetime.strptime(reservation_form['time'].value(),'%H:%M') < datetime.strptime(time,"%H:%M:%S"))):
            messages.add_message(request, messages.ERROR, 'Date or time is invalid, you tried to reserve a table before current time')
        else:    
            reservation = reservation_form.save(commit=False)
            reservation.customer = request.user
            reservation_form.save()
            messages.add_message(request, messages.SUCCESS, 'Reservation added')
            return HttpResponseRedirect(reverse('reservation_list'))          
    reservation_form = ReservationForm()
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


def edit_reservation(request, reservation_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation_form = ReservationForm(data=request.POST, instance=reservation)

        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.date = date
            reservation.time = time
            reservation.area = area
            reservation.have_kids = have_kids
            reservation.note = note
            reservation.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

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