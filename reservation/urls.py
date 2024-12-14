from . import views
# self added
from django.urls import path

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('reservations/',views.reservation_list,name='reservation_list'),
    path('reservations/delete_reservation/<int:reservation_id>',views.delete_reservation, name='delete_reservation'),
    path('reservations/delete_reservations',views.delete_reservations,name='delete_reservations')
]
