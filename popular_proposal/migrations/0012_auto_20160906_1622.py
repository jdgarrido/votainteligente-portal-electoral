# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-06 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popular_proposal', '0011_auto_20160906_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='popularproposal',
            options={'ordering': ['for_all_areas', '-created']},
        ),
    ]
