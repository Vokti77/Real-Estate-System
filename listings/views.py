from django.http import HttpResponse
from django.shortcuts import render


def listings_index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')