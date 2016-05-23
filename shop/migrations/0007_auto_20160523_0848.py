# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_post_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('bet', models.IntegerField(default=0, verbose_name='ставка')),
                ('result', models.CharField(max_length=20, verbose_name='результат')),
            ],
        ),
        migrations.RemoveField(
            model_name='bid',
            name='product',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='bucket',
            field=models.ForeignKey(to='shop.Bucket', null=True),
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.AddField(
            model_name='bet',
            name='product',
            field=models.ForeignKey(to='shop.Post', verbose_name='продукт'),
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
