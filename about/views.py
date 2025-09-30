from django.shortcuts import render
from .models import about_me_model ,my_ability
# Create your views here.

def about_view(request):
    about = about_me_model.objects.filter(is_active=True).first()
    ability = my_ability.objects.filter(is_active=True)

    context ={'about':about,
              'ability':ability,
              }
    return render (request , 'about/about_page.html', context)

