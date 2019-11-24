# Generated by Django 2.1.4 on 2019-11-24 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0004_examconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examconfig',
            name='title',
            field=models.CharField(choices=[('TRADITIONAL', 'TRADITIONAL'), ('EXERCISE', 'EXERCISE'), ('IRAT', 'IRAT'), ('GRAT', 'GRAT'), ('PRACTICAL', 'PRACTICAL'), ('PEER_REVIEW', 'PEER_REVIEW')], default='TRADITIONAL', help_text='Título da avaliação, por exemplo, iRAT, gRAt e etc...', max_length=100, verbose_name='Título da prova'),
        ),
    ]
