from django.shortcuts import render
from django.http import HttpResponse

from .models import Cv


def cv(request):
    send = ""
    if request.method == "POST":

        cv = Cv()

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numero = request.POST.get('numero')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        formation = request.POST.get('formation')
        langue = request.POST.get('langue')
        profil = request.POST.get('profil')
        experience = request.POST.get('experience')
        competence = request.POST.get('competence')
        
        cv.nom = nom
        cv.prenom = prenom
        cv.numero = numero
        cv.email = email
        cv.adresse = adresse
        cv.formation = formation
        cv.langue = langue
        cv.profil = profil
        cv.experience = experience
        cv.competence = competence

        cv.save()

        send = 'Votre candidature a bien été prise en compte !'
        return render(request, 'cv.html', {'send':send})

    return render(request, 'cv.html', {'send':send})
