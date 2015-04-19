# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='preview',
            name='list_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
