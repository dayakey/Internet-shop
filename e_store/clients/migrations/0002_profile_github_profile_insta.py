# Generated by Django 4.1.5 on 2023-01-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='insta',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
