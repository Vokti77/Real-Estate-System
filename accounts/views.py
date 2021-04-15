from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from listings.models import Listing


# Create your views here.


def register(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        first_name = method_dict.get('first_name')
        last_name = method_dict.get('last_name')
        username = method_dict.get('username')
        email = method_dict.get('email')
        password = method_dict.get('password')
        password2 = method_dict.get('password2')

        if password != password2:
            messages.error(request, 'Password does not match!!')
        elif password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                else:
                    User.objects.create_user(
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        email=email
                    )
                    messages.success(request, 'Registration successfully completed!!!')

        return HttpResponseRedirect(reverse('login'))
        # return redirect('login') # alternative

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully Login!!!')
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid Credentials!!')
            return HttpResponseRedirect(reverse('login'))

        # return redirect('login') # alternative

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'Logged out successful!')
    return HttpResponseRedirect(reverse('index'))


def dashboard(request):
    listing_list = Listing.objects.all()
    context = {
        'listing_list': listing_list
    }
    return render(request, 'accounts/dashboard.html', context)
