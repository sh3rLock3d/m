from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery


# Create your views here.
def index(request):
    galleries = Gallery.objects.all().order_by('olaviat')
    print(galleries[0].name, galleries[0].cover_image.url)
    return render(request, 'index.html', {'galleries': galleries})