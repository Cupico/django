from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('base.html')
    return render(request, 'index.html')


def about(request):
    #return HttpResponse('base.html')
    return render(request, 'about.html')