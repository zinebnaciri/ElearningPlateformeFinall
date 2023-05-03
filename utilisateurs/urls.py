from django.urls import path 
from utilisateurs.views import acceuil,user_login, user_logout, register


urlpatterns = [
    path('home/', acceuil, name="acceuil"),
    path('register', register, name="register"),
    path('', user_login, name="login"),
    path('logout', user_logout, name="logout"),
    

]
