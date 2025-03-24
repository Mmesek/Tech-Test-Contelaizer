from django.urls import path

from text_app import views

urlpatterns = [
    path("", views.index, name="index"),
]
