# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiserdetails',
            name='advertise_url',
            field=models.URLField(default=b'www.google.co.in'),
            preserve_default=True,
        ),
    ]
