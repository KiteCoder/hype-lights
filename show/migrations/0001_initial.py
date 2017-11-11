# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamePixel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('action', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('frequency_value', models.FloatField()),
                ('time', models.FloatField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('total_rows', models.IntegerField()),
                ('seats_per_row', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pixel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('grid', models.ForeignKey(to='show.Grid')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='frame',
            name='show',
            field=models.ForeignKey(to='show.Show'),
        ),
        migrations.AddField(
            model_name='famepixel',
            name='frame',
            field=models.ForeignKey(to='show.Frame'),
        ),
        migrations.AddField(
            model_name='famepixel',
            name='pixel',
            field=models.ForeignKey(to='show.Pixel'),
        ),
        migrations.AlterUniqueTogether(
            name='famepixel',
            unique_together=set([('pixel', 'frame')]),
        ),
    ]
