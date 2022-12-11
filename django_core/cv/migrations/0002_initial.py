# Generated by Django 4.1.4 on 2022-12-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('cv', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='pet_projects',
            field=models.ManyToManyField(blank=True, null=True, related_name='cv', to='projects.project'),
        ),
        migrations.AddField(
            model_name='cv',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, related_name='cv', to='tags.tag'),
        ),
    ]
