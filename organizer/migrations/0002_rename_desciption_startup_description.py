# Generated by Django 3.2.8 on 2021-11-04 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='desciption',
            new_name='description',
        ),
    ]
