from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    letest = Listing.objects.order_by('-list_date')[:3]  # 0,1,3 objects //-list_date disorder

    # select * from Listing order by list_date Desc

    return render(request, 'pages/index.html', {'letest':letest})


def about(request):
    team = Realtor.objects.order_by('-contract_date')[:3]
    seller_of_month = Realtor.objects.filter(is_nvp=True).first()
    # Realtor.objects.filter(is_nvp=True) == select * from Realtor where is_nvp=True

    context = {
        'seller_of_month': seller_of_month,
        'team': team
    }
    return render(request, 'pages/about.html',context)


def home(request):
    return HttpResponse("home")


def base(request):
    return render(request, 'base.html')