# Generated by Django 4.0.3 on 2022-07-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_room_name_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
