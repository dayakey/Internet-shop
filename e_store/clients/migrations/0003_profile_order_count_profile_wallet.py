# Generated by Django 4.1.5 on 2023-01-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_profile_github_profile_insta'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='order_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='wallet',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
