# Generated by Django 3.0.5 on 2020-11-24 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_auto_20201124_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='name',
            new_name='uname',
        ),
        migrations.RenameField(
            model_name='ngo',
            old_name='name',
            new_name='uname',
        ),
    ]