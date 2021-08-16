# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Borrow_log(models.Model):
    id=models.AutoField(primary_key=True, unique=True)
    book_id = models.IntegerField(default=0, editable=False)
    borrow_id = models.IntegerField(default=0, editable=False)
    returned = True
    not_returned = False
    Status_option = (
        (returned, 'returned'),
        (not_returned, 'Not returned')
    )
    status = models.BooleanField(
        max_length=10,
        choices=Status_option,
        default=not_returned,
    )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'borrow_log'
        verbose_name = 'Borrow Log'  # Change the module's name

        # To return book_name
    def __str__(self):
        return self.book_id


class Books(models.Model):
    id=models.AutoField(primary_key=True, unique=True)
    book_name= models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    description=models.TextField(max_length=250)
    count = models.IntegerField(default=0, editable=True)
    active = True
    In_active = False
    Status_option = (
        (active, 'Active'),
        (In_active, 'In active')
    )
    status = models.BooleanField(
        max_length=10,
        choices=Status_option,
        default=active,
    )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        verbose_name = 'book'  # Change the module's name

        # To return book_name
    def __str__(self):
        return self.book_name

