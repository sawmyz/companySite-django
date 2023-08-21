from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("add/", views.counseling_add, name="counseling_add"),

]