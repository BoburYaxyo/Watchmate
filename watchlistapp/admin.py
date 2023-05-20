from django.contrib import admin
from watchlistapp.models import Watchlist, StreamPlatform

# Register your models here.
admin.site.register(StreamPlatform)
admin.site.register(Watchlist)
