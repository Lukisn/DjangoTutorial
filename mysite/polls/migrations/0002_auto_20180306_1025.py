# Generated by Django 2.0.2 on 2018-03-06 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]
