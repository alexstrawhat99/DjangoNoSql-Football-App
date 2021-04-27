from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Players
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from products.models import Players

# template pe care le incarc
# trimit request la server

def register_view(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


# def loginPage(request):
#     context = {}
#     return render(request, 'login.html', context)


def login_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'Login.html', {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def transfers_view(request, *args, **kwargs):
    return render(request, "Transfers.html", {})


def homepage_view(request, *args, **kwargs):
    return render(request, "homepage.html", {})


def players_view(request, *args, **kwargs):

    # obj = Players.objects.get(id=1)
    obj = Players.objects.all()
    # obj = Players.objects.order_by('id')
    context = {
        'name': obj,
        'nations': obj,
        'team': obj,
        'city': obj
    }
    return render(request, "Players.html", context)
    # return render("Players.html", context)

# 'city': obj.city