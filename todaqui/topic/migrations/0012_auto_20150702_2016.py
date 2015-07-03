# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0011_auto_20150702_1958'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='topicitem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='topicitem',
            name='topic',
        ),
        migrations.DeleteModel(
            name='TopicItem',
        ),
    ]
