# Generated by Django 2.0.2 on 2018-02-22 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180222_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'get_latest_by': 'originally_published_date', 'ordering': ('originally_published_date',)},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='originally_published_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 22, 18, 25, 19, 501772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='originally_published_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 22, 18, 25, 19, 502963, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
    ]
