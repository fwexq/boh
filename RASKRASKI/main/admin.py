from django.contrib import admin
from .models import *


class pictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'opisanie', 'photo')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(picture, pictureAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Category, CategoryAdmin)