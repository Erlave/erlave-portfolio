from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .models import contact
# Create your views here.




class ContactView(View):
    template_name = 'contact/contact_page.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")

        contact.objects.create(
            name=name,
            email=email,
            massage=massage
        )

        return redirect("home")  # بعد از ذخیره به صفحه موفقیت برو
