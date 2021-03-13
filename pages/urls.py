from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='basep'),




]
