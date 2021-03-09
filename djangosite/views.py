from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    title = "On est sur la homepage"
    #return HttpResponse('base.html')
    return render(request, 'main.html', {"title": title})


def about(request):
    #return HttpResponse('base.html')
    return render(request, 'about.html')