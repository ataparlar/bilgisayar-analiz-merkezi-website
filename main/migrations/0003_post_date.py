# Generated by Django 2.2.12 on 2020-04-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200406_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
