# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-01 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180214_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producer',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='producer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Producer'),
        ),
        migrations.AlterField(
            model_name='consumerrequest',
            name='accepted_producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Producer'),
        ),
        migrations.AlterField(
            model_name='consumerrequest',
            name='consumer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Consumer'),
        ),
        migrations.AlterField(
            model_name='consumerrequest',
            name='timestamp',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Consumer'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
