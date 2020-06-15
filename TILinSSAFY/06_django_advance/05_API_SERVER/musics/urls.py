from django.urls import path
from .import views

app_name = 'musics'

urlpatterns = [
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_id>', views.artist_list, name='artist_list'),

    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_id>', views.music_detail, name='music_detail'),
]