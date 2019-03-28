from django.contrib import admin
from .models import Anime, Episode, Studio, Genre
from .models import Episode

admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Studio)
admin.site.register(Genre)
