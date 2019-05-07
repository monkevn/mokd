# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_member_intro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='scenic',
            name='poster',
        ),
        migrations.AddField(
            model_name='hotel',
            name='tel',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='scenic',
            name='price',
            field=models.FloatField(verbose_name='价格', default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='otype',
            field=models.IntegerField(verbose_name='商品类型', default=0),
        ),
        migrations.AlterField(
            model_name='scenic',
            name='pic',
            field=models.ImageField(verbose_name='景点图片', upload_to='static/upload/'),
        ),
    ]
