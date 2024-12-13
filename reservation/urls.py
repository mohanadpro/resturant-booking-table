from . import views
# self added
from django.urls import path

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('reservations/',views.reservation_list,name='reservation_list')
]
