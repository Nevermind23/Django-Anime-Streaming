from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Anime, Episode
from django.utils.text import slugify
from malparser import MAL


def index(request):
    animes = Anime.objects.all()
    context = {'animes': animes}
    return render(request, 'index.html', context)

def serie(request, id, slug):
    anime = get_object_or_404(Anime, pk=id)
    if slug != slugify(anime.title):
        return redirect('/anime/'+ str(id) +'/'+slugify(anime.title))
    episodes = Episode.objects.filter(anime_id=id).all()
    context = {
        'anime': anime,
        'episodes': episodes,
    }
    return render(request, 'anime.html', context)

def episode(request, id, slug, episode):
    episode = get_object_or_404(Episode, anime_id=id, episode_id=episode)
    context = {'episode': episode}
    return render(request, 'episode.html', context)

def fetch(request):
    return render(request, 'fetch.html')

def fetch(request):
    t = MAL()
    anime = t.get_anime(request.POST['mal_id'])
    anime.fetch()
    
    return redirect('/')
