# Generated by Django 3.2.9 on 2021-12-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0007_featuredproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
