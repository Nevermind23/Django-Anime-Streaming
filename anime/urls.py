from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/<str:slug>', views.serie),
    path('<int:id>/<str:slug>/<int:episode>', views.episode),
    path('fetch', views.fetch),
]
