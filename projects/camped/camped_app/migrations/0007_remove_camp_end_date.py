# Generated by Django 2.2 on 2021-08-24 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camped_app', '0006_camp_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='end_date',
        ),
    ]
