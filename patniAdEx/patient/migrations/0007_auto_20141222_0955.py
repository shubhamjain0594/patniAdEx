# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20141222_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='patient',
            field=models.OneToOneField(to='patient.Patient'),
            preserve_default=True,
        ),
    ]
