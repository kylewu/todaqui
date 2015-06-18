# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_auto_20150617_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32)),
                ('order', models.SmallIntegerField(default=1, unique=True)),
                ('topic', models.ForeignKey(to='topic.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='SubTopicItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('link', models.URLField(max_length=512)),
                ('order', models.SmallIntegerField(default=1, unique=True)),
                ('subtopic', models.ForeignKey(to='topic.SubTopic')),
            ],
        ),
    ]
