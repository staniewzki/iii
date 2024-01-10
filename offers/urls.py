from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('manage/', views.manage, name='manage'),
]