# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patientdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientdetails',
            options={},
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='patient',
        ),
    ]
