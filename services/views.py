from django.shortcuts import render

# Create your views here.
def serv_view(request):
    return render(request ,'serv/serv_page.html')