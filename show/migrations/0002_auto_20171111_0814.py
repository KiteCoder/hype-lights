# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FramePixel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('action', models.TextField()),
                ('frame', models.ForeignKey(to='show.Frame')),
                ('pixel', models.ForeignKey(to='show.Pixel')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='famepixel',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='famepixel',
            name='frame',
        ),
        migrations.RemoveField(
            model_name='famepixel',
            name='pixel',
        ),
        migrations.DeleteModel(
            name='FamePixel',
        ),
        migrations.AlterUniqueTogether(
            name='framepixel',
            unique_together=set([('pixel', 'frame')]),
        ),
    ]
