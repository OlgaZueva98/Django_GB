from django.contrib import admin
from django.urls import path, include
from mainapp import urls
from . import views


urlpatterns = [
    path('products/', views.products),
]
