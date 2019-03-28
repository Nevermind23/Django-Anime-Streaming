from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Anime(models.Model):
    mal_id = models.IntegerField(unique=True)
    vost_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=500)
    geo_title = models.CharField(max_length=500)
    eng_title = models.CharField(max_length=500)
    jp_title = models.CharField(max_length=500)
    description = models.TextField()
    poster = models.ImageField(upload_to='static/posters')
    type = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    studios = models.ManyToManyField(Studio)
    genres = models.ManyToManyField(Genre)
    episodes = models.IntegerField(default=0)
    aired = models.CharField(max_length=500)
    premiered = models.CharField(max_length=500)
    duration = models.CharField(max_length=500)
    rating = models.CharField(max_length=500)
    timer = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    score_rating = models.DecimalField(max_digits=3, decimal_places=2)
    score_votes = models.IntegerField()
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.title

class Episode(models.Model):
    class Meta:
        unique_together = ['anime', 'episode_id']
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    episode_id = models.IntegerField()
    videos_vost = models.TextField(null=True, blank=True)
    videos_manual = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.anime.title+ ' - ' +str(self.episode_id)
