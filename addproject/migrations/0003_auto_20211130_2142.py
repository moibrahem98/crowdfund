# Generated by Django 3.2.9 on 2021-11-30 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0002_auto_20211130_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addproject.projectscategory'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(to='addproject.ProjectsTags'),
        ),
    ]