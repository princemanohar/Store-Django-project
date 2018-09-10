from django.conf.urls import patterns, include, url
from . import views
from myapp.views import StoresListView
from myapp.views import StoreView
urlpatterns = [
    url(r'^storesList', StoresListView.as_view(), name='store-list'),
    url(r'^stores', StoreView.as_view(), name='store'),
    url('', views.stores_list, name='stores_list'),


]