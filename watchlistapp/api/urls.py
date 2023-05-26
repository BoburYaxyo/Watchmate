# from watchlistapp.api.views import movie_details, movie_list
# from watchlistapp.api.views import MovieDetailAV, MovieListAV
from watchlistapp.api.views import StreamPlatformAV, WatchListAV, WatchDetailAV, StreamPlatformDetailAV
from django.urls import path

urlpatterns = [
    # path('list/', MovieListAV.as_view(), name = 'movie_list'),
    # path('list/<int:pk>', MovieDetailAV.as_view(), name = 'single-movie'),
    path('list/', WatchListAV.as_view(), name = 'movie_list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name = 'single-movie'),
    path('stream/', StreamPlatformAV.as_view(), name = 'stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'streamplatform-detail'),
    
]
