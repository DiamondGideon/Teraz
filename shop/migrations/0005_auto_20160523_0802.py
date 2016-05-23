# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_post_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('bet', models.IntegerField(verbose_name='ставка', default=0)),
                ('result', models.CharField(verbose_name='результат', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pic', models.ImageField(upload_to='')),
                ('chield', models.ManyToManyField(to='shop.Category', related_name='chield_rel_+', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='racebet',
            name='race',
        ),
        migrations.RemoveField(
            model_name='racebet',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='result',
        ),
        migrations.RemoveField(
            model_name='post',
            name='win_coef',
        ),
        migrations.AddField(
            model_name='post',
            name='cur_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='discount',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='isAccept',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skype',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name='Автор', to='shop.UserProfile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True, verbose_name='дата публикации', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(verbose_name='Титл', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.IntegerField(verbose_name='баланс', default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='RaceBet',
        ),
        migrations.AddField(
            model_name='bucket',
            name='owner',
            field=models.OneToOneField(to='shop.UserProfile'),
        ),
        migrations.AddField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(verbose_name='продукт', to='shop.Post'),
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(verbose_name='пользователь', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, to='shop.Category'),
        ),
    ]
