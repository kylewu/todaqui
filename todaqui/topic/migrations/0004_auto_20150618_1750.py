# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_subtopic_subtopicitem'),
    ]

    operations = [
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
