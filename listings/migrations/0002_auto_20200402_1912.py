# Generated by Django 3.0.4 on 2020-04-02 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='realotor',
            new_name='realtor',
        ),
    ]
