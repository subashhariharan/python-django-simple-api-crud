# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from books.models import Books


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name','author', 'description', 'status', 'created']  # display category fields
    list_per_page = 15  # set pagination limit
    list_filter = ['book_name', 'description']  # filter category with those fields
    search_fields = ['book_name', 'description']  # search category with those fields

admin.site.register(Books,BookAdmin)