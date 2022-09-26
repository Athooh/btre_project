from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html', {'navbar': 'index'})


def about(request):
    return render(request, 'pages/about.html', {'navbar': 'about'})
