from django.urls import path

from . import views

urlpatterns = [
    path('', views.request, name = 'request'),
    path('itemrequest', views.itemrequest, name = 'itemrequest')

]