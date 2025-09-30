from django.shortcuts import render
from .models import services
# Create your views here.
def serv_view(request):
    serv=services.objects.filter(is_active=True)


    context={'serv':serv,
             }

    return render(request ,'serv/serv_page.html',context)