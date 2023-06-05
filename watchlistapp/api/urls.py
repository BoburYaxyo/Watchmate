# from watchlistapp.api.views import movie_details, movie_list
# from watchlistapp.api.views import MovieDetailAV, MovieListAV
from rest_framework.routers import DefaultRouter
from watchlistapp.api.views import (ReviewCreate, ReviewDetail,ReviewList,
                                    StreamPlatformAV, StreamPlatformVS,WatchListAV, 
                                    WatchDetailAV,StreamPlatformDetailAV)
from django.urls import path, include


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')



urlpatterns = [
    # path('list/', MovieListAV.as_view(), name = 'movie_list'),
    # path('list/<int:pk>', MovieDetailAV.as_view(), name = 'single-movie'),
    path('list/', WatchListAV.as_view(), name = 'movie_list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name = 'single-movie'),
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name = 'stream'),
    
    # path('review/', ReviewList.as_view(), name = 'review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),
    
]
