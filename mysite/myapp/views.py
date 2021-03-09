from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('base.html')
    return render(request, 'index.html')


def contact(request):
    #return HttpResponse('base.html')
    return render(request, 'contact.html')

def blog(request):
    #return HttpResponse('base.html')
    return render(request, 'blog.html')