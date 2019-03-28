from django.contrib import admin
from django.urls import include, path
from anime import views as anime

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', anime.index),
    path('anime/', include('anime.urls')),
]
