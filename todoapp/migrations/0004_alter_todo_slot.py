# Generated by Django 4.2.4 on 2023-08-24 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todo_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='slot',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 6, 48, 0, 172849, tzinfo=datetime.timezone.utc)),
        ),
    ]
