from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from movies.views import ListMovies, MoviesView, AddComment, CommentsView, Top

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^movies/$', ListMovies.as_view(), name='start'),
    url(r'^movies/(?P<pk>[0-9]+)/$', ListMovies.as_view(), name='movie'),
    url(r'^movies/list/$', MoviesView.as_view(), name='movies_list'),
    url(r'^comments/(?P<pk>[0-9]+)/$', AddComment.as_view(), name='comment'),
    url(r'^comments/list/$', CommentsView.as_view(), name='comments_list'),
    url(r'^top/$', Top.as_view(), name='top'),

]
