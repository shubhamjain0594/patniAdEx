# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import patient.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20141222_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cough', models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-1)])),
                ('total_displays', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('patient', models.OneToOneField(to='patient.Patient')),
            ],
            options={
                'ordering': ['patient'],
            },
            bases=(patient.models.ValidateOnSaveMixin, models.Model),
        ),
    ]
