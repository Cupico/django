from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    #return HttpResponse('base.html')
    return render(request, 'blog.html')