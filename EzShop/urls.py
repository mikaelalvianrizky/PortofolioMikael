from django.urls import path
from . import views

app_name = 'EzShop'

urlpatterns = [
    path('', views.index, name='index'),
]