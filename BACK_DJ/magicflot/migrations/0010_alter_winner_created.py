# Generated by Django 4.2.6 on 2024-05-13 18:45

from django.db import migrations, models
import magicflot.models


class Migration(migrations.Migration):

    dependencies = [
        ('magicflot', '0009_winner_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='created',
            field=models.DateTimeField(default=magicflot.models.get_current_timestamp),
        ),
    ]