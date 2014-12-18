# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdate', models.DateTimeField()),
                ('duedate', models.DateTimeField()),
                ('detail', models.CharField(max_length=65535)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.ForeignKey(to='list.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
