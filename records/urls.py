from django.urls import path
from . import views

urlpatterns = [
    path('', views.records_list, name='records_list'),
]

