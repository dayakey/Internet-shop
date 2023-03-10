# Generated by Django 4.1.5 on 2023-01-26 11:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('date', models.DateField(default=datetime.date(2023, 1, 26))),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.goods')),
            ],
        ),
    ]
