# Generated by Django 3.2.7 on 2022-06-10 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamber', '0004_rename_htid_profile_hiveid'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='chamber.profile'),
        ),
    ]