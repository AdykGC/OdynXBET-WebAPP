# Generated by Django 5.0.4 on 2024-05-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(default='Not completed', max_length=50),
        ),
    ]
