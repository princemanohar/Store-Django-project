from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url('', views.stores_list, name='stores_list'),
]