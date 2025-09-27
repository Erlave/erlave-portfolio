from django.urls import path 
from . import views


urlpatterns = [
    path('erlave/' ,views.about_view, name='about'),
]
    

