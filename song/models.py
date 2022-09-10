from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=200)
    slug= models.SlugField()

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='music/%Y/%m/%d/')
    file = models.FileField(upload_to='music/%Y/%m/%d/')
    lyrics = models.TextField()
    artist = models.ForeignKey(Artist,on_delete=models.SET_NULL,related_name='musics')
    
    def __str__(self):
        return self.title