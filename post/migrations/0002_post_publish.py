# Generated by Django 4.0.5 on 2022-06-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
