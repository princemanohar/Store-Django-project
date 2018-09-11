from django.conf.urls import patterns, include, url
from . import views
from myapp.views import StoresListView
from myapp.views import StoreView
from myapp.views import ReviewView
from myapp.views import EntitiesView
from myapp.views import InventoriesView
urlpatterns = [
    url(r'^storesList', StoresListView.as_view(), name='store-list'),
    url(r'^stores', StoreView.as_view(), name='store'),
    url(r'^reviews', ReviewView.as_view(), name='review'),
    url(r'^entities', EntitiesView.as_view(), name='entity'),
    url(r'^inventories', InventoriesView.as_view(), name='inventory'),
    url('', views.stores_list, name='stores_list'),


]