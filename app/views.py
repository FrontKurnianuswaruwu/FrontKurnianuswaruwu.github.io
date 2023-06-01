from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'front',
    }
    return render(request, 'index.html',context)

def tampilanawal(request):
    return render(request, 'tampilanawal.html')

def grid(request):
    return render(request, 'grid.html')

def galeri(request):
    return render(request, 'galeri.html')