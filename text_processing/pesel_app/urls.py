from django.urls import path

from pesel_app import views

urlpatterns = [
    path("", views.index, name="index"),
]
