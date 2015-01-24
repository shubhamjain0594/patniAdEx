# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['username'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvertiserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cough', models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-1)])),
                ('rates', models.DecimalField(default=1, max_digits=10, decimal_places=2)),
                ('total_displays', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('advertiser', models.ForeignKey(to='advertiser.Advertiser')),
            ],
            options={
                'ordering': ['advertiser'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='advertiserdetails',
            unique_together=set([('advertiser', 'cough')]),
        ),
    ]
