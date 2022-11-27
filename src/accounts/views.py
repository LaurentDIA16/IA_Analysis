from django.shortcuts import render, HttpResponse, redirect
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


#Création d'un nouvel Utilisateur avec formulaire basique
class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields

def signup(request):
    context = {}

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Utilisateur créé!'))
            return redirect('home')
            # return HttpResponse("Bienvenue!")
        else:
            context["errors"] = form.errors
    
    form = CustomSignupForm()
    context["form"] = form

    return render(request, "accounts/signup.html", context=context)