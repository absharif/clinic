# Generated by Django 3.2.7 on 2022-06-10 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0006_auto_20220610_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hiveid',
            new_name='hive_id',
        ),
    ]
