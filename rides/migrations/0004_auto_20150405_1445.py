# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_auto_20150405_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='riders',
            field=models.ManyToManyField(to='rides.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.FloatField(default=0, max_length=1),
            preserve_default=True,
        ),
    ]
