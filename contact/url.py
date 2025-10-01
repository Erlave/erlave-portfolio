from django.urls import path 
from . import views


urlpatterns = [
    path('erlave/' ,views.ContactView.as_view(), name='contact'),
]
    

