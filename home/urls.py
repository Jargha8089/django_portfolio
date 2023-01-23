from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('portfolio', portfolio, name='portfolio'),
    path('portfolio-details', details, name='details'),
    path('resume', resume, name='resume'),
    path('services', services, name='services'),
]
