from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'studio'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path('(?P<album_id>[0-9]+)/', views.detail , name= 'detail'),
    path('new-album', views.create_album, name='create_album'),
    path('<int:pk>/update-album', views.AlbumUpdateView.as_view(), name='album-update'),
    path('(?P<album_id>[0-9]+)/album-delete', views.album_delete, name='album-delete'),
    path('(?P<album_id>[0-9]+)/new-song', views.create_song, name='new-song'),
    path('<int:pk>/song-update', views.SongUpdateView.as_view(), name='song-update'),
    path('(?P<album_id>[0-9]+)/song-delete/?P<song_id>[0-9]+/', views.delete_song, name='song-delete'),
]