from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact

def contact(request):
    send = ""
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
        send = 'Merci de nous avoir contacté ! Votre message a bien été reçu'
        return render(request, 'contact.html', {'send':send})
    return render(request, 'contact.html', {'send':send})