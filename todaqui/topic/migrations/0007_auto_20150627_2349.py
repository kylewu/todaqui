# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0006_auto_20150619_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopicitem',
            name='enable',
            field=models.BooleanField(default=True, db_index=True),
        ),
        migrations.AddField(
            model_name='topicitem',
            name='enable',
            field=models.BooleanField(default=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='subtopicitem',
            name='order',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='topicitem',
            name='order',
            field=models.SmallIntegerField(default=1),
        ),
    ]
