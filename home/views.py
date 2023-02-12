from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")    




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