from django.shortcuts import render
from django.conf import settings
import requests
from .forms import SubmitMovie
from .serializer import MovieSerializer


def save_movie(request):

    if request.method == "POST":
        form = SubmitMovie(request.POST)
        if form.is_valid():
            url = form.cleaned_data['title']
            r = requests.get('http://www.omdbapi.com/?apikey=b00ab359&t=' + url)
            json = r.json()
            serializer = MovieSerializer(data=json)
            if serializer.is_valid():
                omdb = serializer.save()
                return render(request, 'db.html', {'omdb': omdb})
    else:
        form = SubmitMovie()

    return render(request, 'index.html', {'form': form})
