# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0010_auto_20150702_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopicitem',
            name='frontpage_order',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='subtopicitem',
            name='shown_in_frontpage',
            field=models.BooleanField(default=False),
        ),
    ]
