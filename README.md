## Conception du projet
![our pro](https://user-images.githubusercontent.com/121731124/236692173-762f4bd6-080e-43f6-9d0f-4b4cef640d01.png)


## Description du projet
- Le projet en Django E-learning consiste en la création d'un site e-learning dynamique et interactif. Ce site permettra aux utilisateurs d'accéder à une plateforme en ligne où ils pourront suivre des cours (Video, telecharger le pdf et la presentation du cours) et acquérir de nouvelles connaissances selon les prerequis de l'école. L'architecture du site est basée sur le framework Django, offrant une structure solide et modulaire pour le développement. Les fonctionnalités clés du site incluent la création de profils d'utilisateurs, la gestion des cours et des modules.  L'interface utilisateur est conviviale et intuitive, offrant une navigation fluide et une expérience d'apprentissage agréable. Le projet s'appuie sur les bonnes pratiques de développement web et utilisera des technologies complémentaires telles que HTML, CSS et JavaScript pour créer un design attrayant et réactif.


### Contenu de chaque dossier.
- elearningplatforme :
    - Est l'application principale de notre projet
- home:
    - c'est lapplication ou se trouve les fonctionnalité de la page Acceuil (CRUD des evenements)
- media:
    - ce dossier contient les medias uploaded de notre projet
- programmes :
    - dans cette application vous trouverez toutes le fonctionnalités permettant CRUD des cours, matieres, lessons ...
- static:
    - ce dossier contient tout les composants de style statiques qu 'on a utilisé (css , js... )
- student:
    - dans cette application vous trouverez toutes le fonctionnalités permettant CRUD des utilisateurs(etudiant ou prof)
- templates:
    - les pages html permettant d'afficher les fonctionnalités developpées 
---
### run the application.
- $ git clone https://github.com/zinebnaciri/ElearningPlateformeFinall.git
- $ cd ElearningPlateformeFinall
- $ python3 -m venv venv
- $ source ./venv/bin/activate
- $ pip3 install -r requirements.txt
- $ python3 manage.py makemigrations
- $ python3 manage.py migrate
- $ python3 manage.py runserver

### Accédez à l'application en ouvrant votre navigateur Web et en accédant à l'URL suivante :
#### http://127.0.0.1:8000
    

### Technologies
<details>
  <summary>Technologies liste </summary>
  
- Django
- djangorestframework
- django-cors-headers
- whitenoise
 

</details>



