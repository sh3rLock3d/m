from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery, Photo


# Create your views here.
def index(request):
    galleries = Gallery.objects.all().order_by('olaviat')

    return render(request, 'index.html', {'galleries': galleries})

def gallery_page(request):
    galleries = Gallery.objects.all().order_by('olaviat')
    category = request.GET.get('category')
    if category:
        photos = Photo.objects.filter(category=Gallery.objects.get(name=category)).order_by('olaviat')
    else:
        photos = Photo.objects.all().order_by('olaviat')
    return render(request, 'category.html', {'galleries': galleries, 'category': category, 'photos':photos})


def about(request):
    return render(request, 'about.html', )


def contact(request):
    return render(request, 'contact.html', )

def services(request):
    return render(request, 'services.html')