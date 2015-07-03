# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0008_auto_20150627_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopicitem',
            name='display_in_frontpage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topicitem',
            name='display_in_frontpage',
            field=models.BooleanField(default=False),
        ),
    ]
