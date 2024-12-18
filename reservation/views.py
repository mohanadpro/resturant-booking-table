from django.shortcuts import render, get_object_or_404, reverse
from .forms import ReservationForm
from .models import Reservation
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def reservation_list(request):
    """
    Display a list of reservations :model:`reservation.Reservation`.
    **Context**
    ``reservations``
        A list of :model:`reservation.Reservation`.
        page_obj to handle pagination
    **Template:**
    :template:`reservation/reservation_list.html`
    """
    temp_reservations = Reservation.objects.filter(
        customer=request.user).order_by("-created_on")
    p = Paginator(temp_reservations, 6)
    page_number = (
        1 if request.GET.get('page')
        is None else request.GET.get('page'))
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'reservations': p.page(page_number)}
    # sending the page object to index.html
    return render(request, 'reservation/reservation_list.html', context)

def check_if_date_and_time_valid(date, selected_time):
    time = str(datetime.now()).split(' ')[1].split('.')[0]
    if (datetime.strptime(
            date,
            '%Y-%m-%d') < datetime.strptime(
                datetime.utcnow().strftime('%Y-%m-%d'),
                '%Y-%m-%d')
                or (
                    datetime.strptime(
                        date,
                        '%Y-%m-%d') == datetime.strptime(
                            datetime.utcnow().strftime('%Y-%m-%d'),
                            '%Y-%m-%d') and
                            (datetime.strptime(
                                selected_time,
                                '%H:%M') <
                                datetime.strptime(time, "%H:%M:%S")))):
        return False
    else:
        return True


def reservation(request):
    """
    Display a list of reservations :model:`reservation.Reservation`.
    **Context**
    ``reservations``
        A list of :model:`reservation.Reservation`.
        page_obj to handle pagination
    **Template:**
    :template:`reservation/reservation_list.html`
    """
    print(' Save ')
    if request.method == "POST":
        # time = str(datetime.now()).split(' ')[1].split('.')[0]
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid() is False:
            messages.add_message(request, messages.ERROR, 'Error happened')
        elif check_if_date_and_time_valid(
            reservation_form['date'].value(),
            reservation_form['time'].value()
        ) is False:    
            messages.add_message(
                request,
                messages.ERROR,
                "Date or time is invalid,"
                + "you tried to reserve a table before current time")
        else:
            reservation = reservation_form.save(commit=False)
            reservation.customer = request.user
            reservation_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Reservation added')
            return HttpResponseRedirect(reverse('reservation_list'))
    reservation_form = ReservationForm()
    return render(
        request,
        "reservation/reserve.html",
        {'reservation_form': reservation_form}
    )


def delete_reservation(request, reservation_id):
    """
    view to delete Reservation
    """
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Reservation is deleted successfully...')
    return HttpResponseRedirect(reverse('reservation_list'))


def edit_reservation(request, reservation_id):
    """
    view to edit reservation
    """
    print(' update ')

    reservation = get_object_or_404(Reservation,pk=reservation_id)
    reservation_form = ReservationForm(initial={
        'how_many_people': reservation.how_many_people,
        'date': reservation.date,
        'time': reservation.time,
        'area': reservation.area,
        'have_kids': reservation.have_kids,
        'special_request': reservation.special_request,
        'note': reservation.note
    })
    if request.method == "POST":
        updated_reservation = get_object_or_404(Reservation,pk=reservation_id)
        reservation_form = ReservationForm(data=request.POST, instance=reservation)
        if reservation_form.is_valid():
            if check_if_date_and_time_valid(
                reservation_form['date'].value(),
                reservation_form['time'].value()) is False:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Date or time is invalid,"
                    + "you tried to reserve a table before current time")
            else:
                updated_reservation = reservation_form.save(commit=False)
                updated_reservation.how_many_people = reservation_form['how_many_people'].value()
                updated_reservation.date = reservation_form['date'].value()
                updated_reservation.time = reservation_form['time'].value()
                updated_reservation.area = reservation_form['area'].value()
                updated_reservation.have_kids = reservation_form['have_kids'].value()
                updated_reservation.special_request = reservation_form['special_request'].value()
                updated_reservation.note = reservation_form['note'].value()
                updated_reservation.save()
                messages.add_message(request, messages.SUCCESS, 'Reservation Updated!')
                return HttpResponseRedirect(reverse('reservation_list'))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error update reservation')
    return render(
        request,
        'reservation/reserve.html',
        {'reservation_form': reservation_form}
    )
