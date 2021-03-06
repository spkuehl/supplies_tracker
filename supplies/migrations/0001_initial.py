# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-21 23:52
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price_bought', models.FloatField(default=0, verbose_name='How much does this cost to buy?')),
                ('reimbursement', models.FloatField(default=0, null=True, verbose_name='How much do you make? (Fill if you sell the items, or provide them against donation)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='whatever')),
            ],
        ),
        migrations.CreateModel(
            name='Items_Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='whatever')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='whatever')),
                ('item', models.ManyToManyField(related_name='Item', through='supplies.Items_Storage', to='supplies.Item')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.Space')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='space',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.User'),
        ),
        migrations.AddField(
            model_name='items_storage',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.Storage'),
        ),
        migrations.AddField(
            model_name='item',
            name='storages',
            field=models.ManyToManyField(related_name='Storage', through='supplies.Items_Storage', to='supplies.Storage'),
        ),
        migrations.AlterUniqueTogether(
            name='items_storage',
            unique_together=set([('storage', 'item')]),
        ),
    ]
