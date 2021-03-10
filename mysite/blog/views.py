from django.shortcuts import render
from django.http import HttpResponse

from .models import Oiseau

def blog(request):
    #return HttpResponse('base.html')
    oiseau = Oiseau.objects.all()
    return render(request, 'blog.html', {'oiseau':oiseau})