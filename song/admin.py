from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# ==================================

# classes
class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('name','slug')
    search_fields = ('name','slug')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',),}
    list_display = ('title','slug')


class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title','slug','artist','category','get_cover')
    search_fields  = ('title','artist__name','category__title')

    def get_cover(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" width="75">')
    get_cover.short_description = 'cover'
    
# Register your models here.

admin.site.register(models.SongVote)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Song,SongAdmin)
admin.site.register(models.Artist,ArtistAdmin)

