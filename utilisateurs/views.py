from django.shortcuts import render
from .forms import UserForm, ProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def acceuil(request):
    return render(request, 'utilisateurs/login.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = ProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered= True
            return HttpResponseRedirect('login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form= UserForm()
        profile_form= ProfileForm()

    content = {
        'registered':registered,
        'form1':user_form,
        'form2':profile_form,
    }
    return render(request, 'utilisateurs/register.html', content)

def user_login(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')

            else:
                return HttpResponse("Utilisateur desactivé ")

        else:
            return HttpResponse("Username ou Password incorrecte ")
    else:
        return render(request, 'utilisateurs/login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



