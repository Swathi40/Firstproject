from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def swathi(request):
    return HttpResponse('it is was executed')
