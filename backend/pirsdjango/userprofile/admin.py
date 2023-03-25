from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location')
    list_filter = ('user', 'bio', 'location')
    search_fields = ('user', 'bio', 'location')
    ordering = ('user', 'bio', 'location')
    filter_horizontal = ()
    list_per_page = 25


admin.site.register(Profile, ProfileAdmin)


