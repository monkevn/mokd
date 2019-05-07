# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181203_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenic',
            name='address',
            field=models.CharField(verbose_name='地址', max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(verbose_name='地址', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='tel',
            field=models.CharField(verbose_name='电话', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='title',
            field=models.CharField(verbose_name='酒店名称', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='scenic',
            name='name',
            field=models.CharField(verbose_name='景点名称', max_length=200, blank=True),
        ),
    ]
