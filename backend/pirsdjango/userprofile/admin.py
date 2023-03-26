from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'phone', 'email')
    list_filter = ('user', 'name', 'address', 'phone', 'email')
    search_fields = ('user', 'name', 'address', 'phone', 'email')
    ordering = ('user', 'name', 'address', 'phone', 'email')
    filter_horizontal = ()
    list_per_page = 25


admin.site.register(Profile, ProfileAdmin)


