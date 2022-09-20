from tabnanny import verbose
# from PIL import Image
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import User
# ====================================================
class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song:category',kwargs={'slug':self.slug})  

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)


    
    class Meta:
        verbose_name_plural = 'categories'

# ====================================================

class Artist(models.Model):
    name = models.CharField(max_length=200)
    slug= models.SlugField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('song:artist',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)



# ====================================================

class Song(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.CharField(max_length=400,blank=True,null=True)
    image = models.ImageField(upload_to='music/%Y/%m/%d/')
    file = models.FileField(upload_to='music/%Y/%m/%d/',blank=True,null=True)
    lyrics = models.TextField()
    artist = models.ForeignKey(Artist,on_delete=models.DO_NOTHING,related_name='songs')
    created_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('category',on_delete=models.DO_NOTHING,related_name='songs')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # if self.image:
        #     img = Image.open(self.image.path)
        #     img.thumbnail((200,200))
        #     img.save(self.image.path)
        return super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('song:detail',kwargs={'pk':self.pk,'slug':self.slug})

    def get_vote_count(self):
        return self.votes.count()

    
# ====================================================
class SongVote(models.Model):
    user = models.ForeignKey(User ,on_delete=models.DO_NOTHING,related_name='votes')
    song = models.ForeignKey(Song ,on_delete=models.CASCADE,related_name='votes')

    def __str__(self):
        return f'{self.user} voted for {self.song.title}'
