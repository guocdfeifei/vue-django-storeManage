# Generated by Django 2.2.5 on 2020-01-01 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20200101_1102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Origanization',
            new_name='Organization',
        ),
        migrations.RenameField(
            model_name='centerwarehouse',
            old_name='origanization',
            new_name='organization',
        ),
    ]
