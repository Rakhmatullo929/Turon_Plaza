# Generated by Django 4.0.3 on 2022-07-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
