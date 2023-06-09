from django.shortcuts import render, redirect
from .forms import RegisterForm,IngredientForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import testcalc

@login_required(login_url="/login")
def home(request):
    ingredients = []
    score = 0
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients'].split(',') # split the comma-separated ingredients into a list
            # Do something with the list of ingredients
            score = testcalc.calc_ing(ingredients)
    return render(request, 'main/home.html', {'form': form, 'ingredients': ingredients,'score':score})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    

    return render(request, 'registration/sign_up.html', {"form": form})