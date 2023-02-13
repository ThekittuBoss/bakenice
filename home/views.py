from django.shortcuts import render, redirect
from .models import Contact, menuIteam
# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")    

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            return redirect('success')
    return render(request, 'contact.html')


def success_view(request):
    return render(request, 'success.html')

def menu(request):
    menuitem = menuIteam.objects.all()
    context = {'menuitem': menuitem}
    return render(request, 'menu.html', context)
