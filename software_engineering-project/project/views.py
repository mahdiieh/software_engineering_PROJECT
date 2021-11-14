from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Movie
import requests
import json


def home(request):
    movies = Movie.objects.all()
    # index = 0
    # movieName = []
    # image = []
    # for i in movies:
    #     movieName.append(i.title)
    # url = "https://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query={}"
    # purl = "http://image.tmdb.org/t/p/w500"
    # for i in movieName:
    #     resp = requests.get(url+i).json()
    #     poster = resp['results']['poster_path']
    #     img = requests.get(purl+poster)
    #     image.append(img)
    #     movies[index].imageUrl = img
    #     index += 1
    return render(request, 'project/home.html', {'movies': movies})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'project/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'project/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'That username has already been taken.Please try another one.'})

        else:
            return render(request, 'project/signupuser.html', {'form': UserCreationForm(), 'error': 'passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'project/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'project/loginuser.html', {'form': AuthenticationForm(), 'error':'username and password did not match.'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
