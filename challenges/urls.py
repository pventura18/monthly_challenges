from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>/", views.montyly_chanllenge_number),
    path("<str:month>/", views.montyly_chanllenge, name="month-challenge"),
    
]