from django.urls import path

from suosuo import views

urlpatterns = [
    path('', views.index, name="index"),

]