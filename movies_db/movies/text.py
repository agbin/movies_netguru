from django.shortcuts import render
from django.conf import settings
import requests
from .forms import SubmitMovie
from .serializer import MovieSerializer
from rest_framework import generics
from .models import Movie
from rest_framework.views import APIView
from rest_framework.response import Response


# class MoviesView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class ListMovies(APIView):

    def get(self, request, format=None):

        form = SubmitMovie()



        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        # return Response(serializer_class)
        return render(request, 'index.html', {'form': form})

    def post(self, request, format=None):

        # if request.method == "POST":
        form = SubmitMovie(request.POST)
        if form.is_valid():
            url = form.cleaned_data['title']
            r = requests.get('http://www.omdbapi.com/?apikey=b00ab359&t=' + url)
            json = r.json()
            # data_json = {
            #     "Title": json['Title'],
            #     "Title": json['Title'],
            # }
            serializer = MovieSerializer(data=json)
            if serializer.is_valid():
                omdb = serializer.save()
            return render(request, 'db.html', {'omdb': omdb})
