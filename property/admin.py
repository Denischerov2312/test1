from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'adress')
    readonly_fields = ('created_at',)


admin.site.register(Flat, FlatAdmin)
