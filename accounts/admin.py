from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from . import forms
from django.contrib.auth.models import Group

# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    list_display = ('email','is_admin','is_pro')
    list_filter = ('is_admin','is_pro')
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin','is_pro')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()
    
admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

admin.site.site_header = 'MusicOnline | administrator'
# admin.site.site_title = ' Dashbord '
admin.site.index_title = 'MusicOnline | administrator'