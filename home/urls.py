from . import views
from django.urls import path

urlpatterns = [
    path('', views.MarketList.as_view(), name='home'),
]