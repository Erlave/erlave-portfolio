from django.urls import path 
from . import views


urlpatterns = [
    path('erlave/' ,views.port_view, name='portfolio'),
]
    

