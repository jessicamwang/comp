# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.RemoveField(
            model_name='image',
            name='content',
        ),
    ]
