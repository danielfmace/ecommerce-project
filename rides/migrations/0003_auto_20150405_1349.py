# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0002_auto_20150405_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.OneToOneField(to='rides.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('seats', models.IntegerField(max_length=2)),
                ('taken', models.IntegerField(max_length=2)),
                ('dest', models.OneToOneField(to='rides.Dest')),
                ('driver', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.OneToOneField(to='rides.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='university',
            name='location',
        ),
        migrations.DeleteModel(
            name='University',
        ),
        migrations.AddField(
            model_name='ride',
            name='start',
            field=models.OneToOneField(to='rides.Start'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=200, default='Name'),
            preserve_default=True,
        ),
    ]
