from django.contrib import admin
from django.urls import path
from django.urls import include, path
from main import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create',views.create,name="create"),
    path('<str:url>',views.redirect,name="redirect")
]

