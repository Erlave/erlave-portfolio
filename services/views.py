from django.shortcuts import render

# Create your views here.
def serv_page(request):
    return render(request ,'serv/serv_page.html')