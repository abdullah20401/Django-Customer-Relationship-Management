# Generated by Django 3.1.3 on 2020-12-01 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201201_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='notes',
            new_name='note',
        ),
    ]
