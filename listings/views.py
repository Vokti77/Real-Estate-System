from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from .models import Listing
from .model_choices import *


def listings_index(request):
    listing_list = Listing.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(listing_list, 2)

    try:
        listing_list = paginator.page(page)

    except PageNotAnInteger:
        # fall back to first page
        listing_list = paginator.page(1)
    except EmptyPage:
        # fall back to last page
        listing_list = paginator.page(paginator.num_pages)

    context = {
        'listing_list': listing_list
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_ = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing.html', {'listing':listing_})


def search(request):
    listing_list = Listing.objects.all()
    method_dict = request.GET.copy()
    keywords = method_dict.get('keywords') or None
    city = method_dict.get('city') or None
    sqft = method_dict.get('sqft') or None
    page = request.GET.get('page', 1)
    paginator = Paginator(listing_list, 3)

    if keywords is not None:
        keyword = method_dict['keywords']
        # listing_list = listing_list.filter(desc__iexact=keyword)  # django == DJANGO
        listing_list = listing_list.filter(desc__icontains=keyword)  # django == Django Web development

    if city is not None:
        cities = method_dict['city']
        listing_list = listing_list.filter(city__iexact=cities)

    if sqft is not None:
        sqfts = method_dict['sqft']
        listing_list = listing_list.filter(sqft__lte=int(sqfts))

    if 'state' in method_dict:
        states = method_dict['state']
        listing_list = listing_list.filter(state__iexact=states)

    if 'bedrooms' in method_dict:
        bedroom = method_dict['bedrooms']
        listing_list = listing_list.filter(bedrooms__lte=int(bedroom))  # 5<= 1, 2, 3, 4, 5

    if 'price' in method_dict:
        prices = method_dict['price']
        listing_list = listing_list.filter(price__lte=int(prices))

    try:
        listing_list = paginator.page(page)

    except PageNotAnInteger:
        # fall back to first page
        listing_list = paginator.page(1)
    except EmptyPage:
        # fall back to last page
        listing_list = paginator.page(paginator.num_pages)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'method_dict': method_dict,
        'listing_list': listing_list
    }

    return render(request, 'listings/search.html', context)