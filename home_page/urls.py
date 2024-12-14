from . import views
# self added
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home_page')
]
