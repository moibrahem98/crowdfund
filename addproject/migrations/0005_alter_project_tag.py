# Generated by Django 3.2.9 on 2021-12-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0004_auto_20211201_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(to='addproject.ProjectsTags'),
        ),
    ]
