from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from movie.models import *
import operator
import random
from movie.initializer import search_index
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
        if user is None:
            return render(request, 'project/loginuser.html', { 'error':'Username or password is incorrect.'})
        else:
            login(request, user)
            return redirect('/movie/movie_all/1')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/movie/movie_all/1')
            except IntegrityError:
                return render(request, 'signupuser.html',
                              {'form': UserCreationForm(), 'error': 'this username has already taken'})
        else:
            return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'passwords did not match.'})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

@csrf_protect
def index(request):
    data = {}
    movie_dict = search_index.data_in_memory['movie_dict']
    if request.user.is_authenticated:
        data = {'username': request.user.get_username()}
    popular_movies = Popularity.objects.all().order_by('-weight')
    popular = []
    for movie in popular_movies[:5]:
        try:
            popular.append({'movieid': movie.movieid_id, 'poster': movie_dict[movie.movieid_id].poster})
        except:
            continue
    data['popular'] = popular
    popular_movie_list = [movie_dict[movie.movieid_id] for movie in popular_movies[:5]]
    data['recommendation'] = get_recommendation(request, popular_movie_list)
    return render(request, 'base.html', data)


def get_recommendation(request, popular_movie_list):
    result = []
    movie_dict = search_index.data_in_memory['movie_dict']
    added_movie_list = []
    if request.user.is_authenticated:
        username = request.user.get_username()
        watched_movies = set([movie_dict[movie.movieid_id] for movie in Seen.objects.filter(username=username)] +
                             [movie_dict[movie.movieid_id] for movie in Expect.objects.filter(username=username)])
        unwatched_movies = set(search_index.data_in_memory['movie_list']) - watched_movies - set(popular_movie_list)
        genre_stats = {}
        for movie in watched_movies:
            for genre in movie.genres.split('|'):
                genre_stats[genre] = genre_stats.get(genre, 0) + 1
        movie_score = {}
        for movie in unwatched_movies:
            movie_score[movie.movieid] = movie.rate
            for genre in movie.genres.split('|'):
                movie_score[movie.movieid] += genre_stats.get(genre, 0) / len(watched_movies)
        sorted_list = sorted(movie_score.items(), key=operator.itemgetter(1), reverse=True)
        for item in sorted_list:
            movie = movie_dict[item[0]]
            result.append({'movieid': movie.movieid, 'poster': movie.poster})
            added_movie_list.append(movie)
            if len(result) == 8:
                break
    sorted_list = sorted(search_index.data_in_memory['movie_rating'].items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_list:
        movie = movie_dict[item[0]]
        if movie not in popular_movie_list and movie not in added_movie_list:
            result.append({'movieid': movie.movieid, 'poster': movie.poster})
        if len(result) == 10:
            break
    return [result[i] for i in random.sample(range(len(result)), 5)]
