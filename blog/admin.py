# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.contrib import admin

from django.contrib import admin
from .models import Post 



# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

