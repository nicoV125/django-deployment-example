# Generated by Django 3.0.3 on 2020-05-05 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfoloio_site',
            new_name='portfolio_site',
        ),
    ]
