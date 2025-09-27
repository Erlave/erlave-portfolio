from django.urls import path 
from . import views


urlpatterns = [
    path('erlave/' ,views.serv_page, name='services'),
]
    

