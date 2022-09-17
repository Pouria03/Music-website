from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = ''
    add_form = ''

    list_display = ('email','is_admin','is_pro','is_staff')
    list_filter = ('is_admin','is_pro')
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin','is_staff','is_pro')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.register(User,UserAdmin)
admin.site.site_header = 'MusicOnline | administrator'
admin.site.site_title = ' MusicOnline '

# admin.site.index_title = ' your index title'