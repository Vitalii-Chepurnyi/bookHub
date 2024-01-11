from . import views
from django.urls import path

urlpatterns = [
    path('', views.MarketList.as_view(), name='home'),
    path('<slug:slug>/', views.listing_detail, name='listing_detail'),
]