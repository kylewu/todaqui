# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotsite', '0002_auto_20150627_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotsite',
            name='order',
            field=models.SmallIntegerField(default=1),
        ),
    ]
