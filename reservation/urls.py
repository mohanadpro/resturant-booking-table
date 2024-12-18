from . import views
# self added
from django.urls import path

urlpatterns = [
    path(
        '',
        views.reservation_list,
        name='reservation_list'),
    path(
        'reserve/',
         views.reservation,
         name='reservation'),
    path(
        'delete_reservation/<int:reservation_id>',
        views.delete_reservation,
        name='delete_reservation'),
    path(
        'edit_reservation/<int:reservation_id>',
        views.edit_reservation,
        name='edit_reservation'),
]
