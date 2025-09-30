from django.shortcuts import render
from .models import services,plan_title,plan_cart
# Create your views here.
def serv_view(request):
    serv=services.objects.filter(is_active=True)
    plan=plan_title.objects.filter(is_active=True).first()
    cart=plan_cart.objects.filter(is_active=True)

    context={'serv':serv,
             'plan':plan,
             'cart':cart
             }

    return render(request ,'serv/serv_page.html',context)