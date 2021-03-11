# django2

Interface django:

Arborescence générale:

-mysite
| |
|--Home
| |
|--Blog
| |
|--Contact
| |
|--Cv
| |
|--mysite
|
-manager.py

Contenu :

1- Page d'accueil:

Une simple homepage, une banière avec une image d'oiseau et d'autres images d'oiseau en dessous.

2- Blog projet:

Articles avec les noms d'oiseaux, leur date de publication (journée année et heure), image et description. On les affiche depuis la base de données, où ils sont enregistrés. On peut les éditer/ajouter/supprimer du côté admin, dans la section "Oiseaux". On peut ajouter un oiseau, il va directement être affiché sur le blog.

3- Formulaire de contact:

Avec nom, mail, sujet et message. On les reçoit bien en admin, on peut visualiser tous les formulaires de contact que l'on a reçu du côté admin dans la section "Contact".

4- Candidature:

Template de CV qu'on peut remplir (nom, prénom, description du profil, expériences et compétences... ). On reçoit ainsi toutes les candidatures du côté admin, dans la section "CV".

Admin:

Identifiants de connexion : elbardavid / mdp: Dofusien19

En ajoutant /admin derrière l'URL originel du site, on obtient l'accès à la base de données où l'on peut observer, ajouter, éditer et supprimer facilement et simplement toutes les sections citées plus haut (oiseaux, formulaire de contact et candidatures). 


Projet réalisé par David Elbar & Amaury Gimonnet.
