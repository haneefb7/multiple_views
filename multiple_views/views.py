from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mobile(request):
    return HttpResponse('the Latest Mobile of Iphone is Iphone 16 pro max')

def earbuds(request):
    return HttpResponse('<h1>The Best Earbuds company is JBL</h1>')

def laptop(request):
    return HttpResponse('<h1><marquee>Dell is a good laptop</marquee></h1>')