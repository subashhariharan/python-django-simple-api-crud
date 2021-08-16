# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-26 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('book_id', models.IntegerField(default=0, editable=False)),
                ('borrow_id', models.IntegerField(default=0, editable=False)),
                ('status', models.BooleanField(choices=[(True, 'returned'), (False, 'Not returned')], default=False, max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'borrow_log',
                'verbose_name': 'Borrow Log',
            },
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'book'},
        ),
        migrations.AlterField(
            model_name='books',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
