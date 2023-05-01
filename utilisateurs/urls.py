from django.urls import path 
from utilisateurs.views import acceuil,user_login, user_logout, register

urlpatterns = [
    path('', acceuil, name="acceuil"),
    path('register', register, name="register"),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),

]
