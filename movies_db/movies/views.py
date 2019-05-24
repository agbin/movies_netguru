from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import SubmitMovie
from .serializer import MovieSerializer, CommentSerializer, MovieTopSerializer
from rest_framework import generics
from .models import Movie, Comment
from .forms import CommentAddForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.db.models import Count
from django.db.models import F



class ListMovies(APIView):
    # Add movie
    def get(self, request):

        form = SubmitMovie()
        return render(request, 'index.html', {'form': form})

    def post(self, request):

        form = SubmitMovie(request.POST)
        if form.is_valid():
            url = form.cleaned_data['title']
            r = requests.get('http://www.omdbapi.com/?apikey=b00ab359&t=' + url)
            json = r.json()
            serializer = MovieSerializer(data=json)
            if serializer.is_valid():
                omdb = serializer.save()
            return render(request, 'db.html', {'omdb': omdb})
        form = SubmitMovie()
        return render(request, 'index.html', {'form': form})



class MoviesView(generics.ListCreateAPIView):
    # List of all recorded movies
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class AddComment(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        comments = Comment.objects.filter(movie=pk)
        form = CommentAddForm
        return render(request, 'comment.html', {'movie': movie, 'comments': comments, "form": form})

    def post(self, request, pk):
        form = CommentAddForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data['text'],
                movie=movie,
                name=form.cleaned_data['name'],
            )
            Movie.objects.filter(pk=pk).update(Total_comments=F('Total_comments') + 1)
            return redirect('comment', pk)


class CommentsView(generics.ListCreateAPIView):
    # List of all recorded movies
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class Top(generics.ListCreateAPIView):
    top_movies = Movie.objects.all().order_by('-Total_comments')
    top_list = []
    rank = 0
    prev_rank = 0
    for movie in top_movies:
        if movie.Total_comments != prev_rank:
            prev_rank = movie.Total_comments
            rank += 1
        top_list.append({
            'movie_id': movie.pk,
            'total_comments': movie.Total_comments,
            'rank': rank
        })
    queryset = top_list
    serializer_class = MovieTopSerializer