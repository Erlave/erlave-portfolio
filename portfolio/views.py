from django.shortcuts import render

# Create your views here.
def port_view(request):
    return render(request ,'portfolio/portfolio_page.html')