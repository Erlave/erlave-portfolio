from django.urls import path 
from . import views


urlpatterns = [
    path('erlave/' ,views.contact_view, name='contact'),
]
    

