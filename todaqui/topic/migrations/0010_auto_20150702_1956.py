# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0009_auto_20150702_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopicitem',
            name='display_in_frontpage',
        ),
        migrations.RemoveField(
            model_name='topicitem',
            name='display_in_frontpage',
        ),
    ]
