from django.shortcuts import render
from .models import about_me_model
# Create your views here.

def about_view(request):
    about = about_me_model.objects.filter(is_active=True).first()
    context ={'about':about,
              }
    return render (request , 'about/about_page.html', context)

