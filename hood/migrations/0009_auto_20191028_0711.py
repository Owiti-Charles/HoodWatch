# Generated by Django 2.2.6 on 2019-10-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]