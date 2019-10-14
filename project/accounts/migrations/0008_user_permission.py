# Generated by Django 2.1.4 on 2019-10-14 03:14

import accounts.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191002_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permission',
            field=models.CharField(default=accounts.enum.PermissionSet(('STUDENT',)), help_text='Verifica o tipo de permissão que o usuário tem.', max_length=50, verbose_name='Permissão.'),
        ),
    ]