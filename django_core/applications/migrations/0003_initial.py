# Generated by Django 4.1.4 on 2022-12-11 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0002_initial'),
        ('user_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_core.student'),
        ),
    ]
