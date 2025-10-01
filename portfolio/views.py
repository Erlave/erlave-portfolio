from django.shortcuts import render
from .models import prot_title,portfolio
# Create your views here.
def port_view(request):
    title=prot_title.objects.filter(is_active=True).first()
    port=portfolio.objects.filter(is_active=True)
    context={'title':title,
             'port':port
             }



    return render(request ,'portfolio/portfolio_page.html',context)