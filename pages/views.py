from django.shortcuts import render
from listings.models import listing
from listings.models import Realtor
# Create your views here.


def index(request):
    listings = listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'navbar': 'index'
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'navbar': 'about'
    }
    return render(request, 'pages/about.html', context)
