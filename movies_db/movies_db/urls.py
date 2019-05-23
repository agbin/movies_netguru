from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from movies.views import save_movie

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', save_movie),
]
