from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("receipt",views.receipt),
    path("checkout", views.checkout),
]