# Generated by Django 4.1.4 on 2022-12-10 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]