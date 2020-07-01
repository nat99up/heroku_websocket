from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.cache import cache 

def index(request,name='Guest'):

    last_guest = cache.get('last_guest')

    cache.set('last_guest',name)

    return HttpResponse('Hi {}! I am bot. \n Last guest is {}.'.format(name,last_guest))