from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('add-offer/', views.add_offer, name='add_offer'),
    path('book/<int:offer_id>', views.book, name='book'),
    path('manage/', views.manage, name='manage'),
]