from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import *

class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_url', 'created', 'is_show')
    list_filter = ('is_show',)
    list_per_page = 20
    search_fields = ['title']

admin.site.register(Banner, BannerAdmin)
