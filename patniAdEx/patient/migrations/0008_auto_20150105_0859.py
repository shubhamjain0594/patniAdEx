# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_auto_20141222_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='cough',
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='url',
            field=models.URLField(default=-1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-1)]),
            preserve_default=True,
        ),
    ]
