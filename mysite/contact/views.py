from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact

def contact(request):
    #return HttpResponse('base.html')
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse('<h2>Merci de nous avoir contacté !</h2>')
    return render(request, 'contact.html')