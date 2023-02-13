from django.shortcuts import render, redirect
from home.models import menuIteam

# Create your views here.
def dashboard(requset):
    return render(requset,'dashboard/sidebar.html')


def addpost(request):
    if request.method =='POST':
        Item_name = request.POST.get('Item_name')
        img = request.FILES.get('img')
        desc = request.POST.get('desc')
        addblog = menuIteam(Item_name=Item_name, img=img, desc= desc)
        addblog.save()
        return redirect('home')
    return render(request, 'dashboard/add.html')    
