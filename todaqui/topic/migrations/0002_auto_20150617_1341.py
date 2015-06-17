# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='order',
            field=models.SmallIntegerField(default=1, unique=True),
        ),
        migrations.AddField(
            model_name='topicitem',
            name='order',
            field=models.SmallIntegerField(default=1, unique=True),
        ),
    ]
