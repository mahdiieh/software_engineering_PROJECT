from django.test import TestCase
from .models import Movie, Actor, Act, Popularity
from django.contrib.auth.models import User


class Main_Test(TestCase):
    def test_movie_fileds(self):
        movie = Movie()
        movie.title = "Test"
        movie.year = 1980
        movie.length = 150
        movie.genres = "Action"
        movie.rate = 6.8
        movie.poster = "https://www.imdb.com/title/tt0378407/mediaviewer/rm3771205376/"
        movie.plot = "Since the second grade, Brian has had a crush on Drew Barrymore and now 20 years later he wants to fulfill his dream by asking her on a date."
        movie.trailer = "https://www.imdb.com/video/vi211288345?playlistId=tt0378407&ref_=tt_ov_vi"
        movie.save()

        record = Movie.objects.get(pk=1)

        self.assertEqual(record, movie)

    def test_actor_fields(self):
        actor = Actor()
        actor.actorid = 1
        actor.name = "TestActor"
        actor.photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Johnny_Depp_Deauville_2019.jpg/640px-Johnny_Depp_Deauville_2019.jpg"
        actor.save()

        record = Actor.objects.get(pk=1)

        self.assertEqual(record, actor)

    def test_act(self):
        movie = Movie()
        movie.title = "Test"
        movie.year = 1980
        movie.length = 150
        movie.genres = "Action"
        movie.rate = 6.8
        movie.poster = "https://www.imdb.com/title/tt0378407/mediaviewer/rm3771205376/"
        movie.plot = "Since the second grade, Brian has had a crush on Drew Barrymore and now 20 years later he wants to fulfill his dream by asking her on a date."
        movie.trailer = "https://www.imdb.com/video/vi211288345?playlistId=tt0378407&ref_=tt_ov_vi"
        movie.save()

        actor = Actor()
        actor.actorid = 1
        actor.name = "TestActor"
        actor.photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Johnny_Depp_Deauville_2019.jpg/640px-Johnny_Depp_Deauville_2019.jpg"
        actor.save()

        act = Act()

        act.movieid = movie
        act.actorid = actor

        act.save()

        record = Act.objects.get(pk=1)

        self.assertEqual(record, act)

    def test_popularity(self):
        movie = Movie()
        movie.title = "Test"
        movie.year = 1980
        movie.length = 150
        movie.genres = "Action"
        movie.rate = 6.8
        movie.poster = "https://www.imdb.com/title/tt0378407/mediaviewer/rm3771205376/"
        movie.plot = "Since the second grade, Brian has had a crush on Drew Barrymore and now 20 years later he wants to fulfill his dream by asking her on a date."
        movie.trailer = "https://www.imdb.com/video/vi211288345?playlistId=tt0378407&ref_=tt_ov_vi"
        movie.save()

        pop = Popularity()

        pop.movieid = movie

        pop.weight = 5

        pop.save()

        record = Popularity.objects.get(pk=1)

        self.assertEqual(record, pop)

    def test_seen_response(self):
        movie = Movie()
        movie.title = "Test"
        movie.year = 1980
        movie.length = 150
        movie.genres = "Action"
        movie.rate = 6.8
        movie.poster = "https://www.imdb.com/title/tt0378407/mediaviewer/rm3771205376/"
        movie.plot = "Since the second grade, Brian has had a crush on Drew Barrymore and now 20 years later he wants to fulfill his dream by asking her on a date."
        movie.trailer = "https://www.imdb.com/video/vi211288345?playlistId=tt0378407&ref_=tt_ov_vi"
        movie.save()

        response = self.client.get('seen/1')

        self.assertTemplateUsed(response, 'seen.html')


