from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('base.html')
    return render(request, 'main.html')