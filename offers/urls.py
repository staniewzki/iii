from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('book/<int:offer_id>', views.book, name='book'),
    path('manage/', views.manage, name='manage'),
]