# Generated by Django 4.1.4 on 2022-12-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
