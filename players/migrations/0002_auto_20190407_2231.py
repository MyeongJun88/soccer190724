# Generated by Django 2.0.13 on 2019-04-07 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='players',
            old_name='price',
            new_name='age',
        ),
    ]
