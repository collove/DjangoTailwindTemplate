from django.urls import path

from . import views

urlpatterns = [
    path("", views.home.as_view(), name="home"),
]
