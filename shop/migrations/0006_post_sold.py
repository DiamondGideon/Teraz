# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20160523_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
