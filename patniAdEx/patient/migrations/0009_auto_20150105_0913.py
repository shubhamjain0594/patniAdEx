# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20150105_0859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientdetails',
            options={'ordering': ['ip']},
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='total_displays',
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='ip',
            field=models.GenericIPAddressField(default='0:0:0:0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
