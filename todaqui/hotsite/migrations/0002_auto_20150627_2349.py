# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotsite',
            name='enable',
            field=models.BooleanField(default=True, db_index=True),
        ),
        migrations.AddField(
            model_name='hotsite',
            name='order',
            field=models.SmallIntegerField(default=1),
        ),
    ]
