# Generated by Django 2.2 on 2021-08-05 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camped_app', '0002_auto_20210805_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
