from django.shortcuts import render
from .models import hi , home_model
# Create your views here.

def home_view(request):
    hello = hi.objects.filter(is_active=True)
    home = home_model.objects.filter(is_active=True).first()
    context = {'hello':hello,
               'home':home}
    return render (request , 'homes/home_page.html' ,context)




def footer_componnent(request):
    return render(request,'footer_componnent.html')

def header_componnent(request):
    return render(request,'header_componnent.html')



