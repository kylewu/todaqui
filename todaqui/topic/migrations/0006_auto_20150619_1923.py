# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_auto_20150618_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='enable',
            field=models.BooleanField(default=True, db_index=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='enable',
            field=models.BooleanField(default=True, db_index=True),
        ),
    ]
