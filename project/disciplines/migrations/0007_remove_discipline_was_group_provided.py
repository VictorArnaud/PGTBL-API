# Generated by Django 2.1.4 on 2019-10-20 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplines', '0006_discipline_was_group_provided'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipline',
            name='was_group_provided',
        ),
    ]
