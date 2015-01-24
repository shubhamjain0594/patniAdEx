# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='patient',
        ),
        migrations.DeleteModel(
            name='PatientDetails',
        ),
    ]
