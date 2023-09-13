from django.shortcuts import render,redirect
from .models import Image

# Create your views here.

def index(request):
    images = Image.objects.all()
    context = {
        'images' : images
    }
    return render(request,'home/index.html',context)

def upload(request):
    if request.method == 'POST':
        name = request.POST['name']
        about = request.POST['about']
        photo = request.FILES.get('photo')
        item = Image(name=name,about=about,photo=photo)
        item.save()
        return redirect('index')
    else:
        return render(request,"home/addimage.html")
