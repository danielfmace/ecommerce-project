# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.ForeignKey(to='rides.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
