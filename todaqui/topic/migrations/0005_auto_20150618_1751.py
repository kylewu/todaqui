# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_auto_20150618_1750'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subtopicitem',
            unique_together=set([('subtopic', 'order')]),
        ),
        migrations.AlterUniqueTogether(
            name='topicitem',
            unique_together=set([('topic', 'order')]),
        ),
    ]
