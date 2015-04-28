# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, default='Name')),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(max_length=1, default=0)),
                ('comments', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(max_length=2)),
                ('taken', models.IntegerField(max_length=2, default=0)),
                ('time', models.DateTimeField(default=datetime.datetime.today)),
                ('dest', models.ForeignKey(to='rides.Dest')),
                ('driver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.OneToOneField(to='rides.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('has_car', models.BooleanField(default=True)),
                ('seats', models.IntegerField(max_length=2)),
                ('rating', models.FloatField(max_length=1, default=0)),
                ('phone', models.IntegerField(max_length=10)),
                ('avatar', models.ImageField(null=True, upload_to='images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ride',
            name='riders',
            field=models.ManyToManyField(null=True, blank=True, to='rides.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ride',
            name='start',
            field=models.ForeignKey(to='rides.Start'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(to='rides.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='ride',
            field=models.ForeignKey(to='rides.Ride'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dest',
            name='location',
            field=models.OneToOneField(to='rides.Location'),
            preserve_default=True,
        ),
    ]
