# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0002_advertiserdetails_advertise_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiserdetails',
            name='advertise_url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
