# Generated by Django 2.1.4 on 2019-09-21 20:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of discipline', max_length=100, verbose_name='Title')),
                ('institution', models.CharField(help_text='University or School in which the user is inserted.', max_length=100, verbose_name='Institution')),
                ('course', models.CharField(help_text='Course that is ministered the discipline', max_length=100, verbose_name='Course')),
                ('description', models.TextField(help_text='Description of discipline', verbose_name='Description')),
                ('classroom', models.CharField(default='Class A', help_text='Classroom title of discipline.', max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^Class|^Turma [A-Z]$'), "Enter a valid classroom, the classroom need to be 'Class A-Z'")], verbose_name='Classroom')),
                ('password', models.CharField(blank=True, help_text='Password to get into the class.', max_length=30, verbose_name='Password')),
                ('students_limit', models.PositiveIntegerField(default=0, help_text='Students limit to get in the class.', validators=[django.core.validators.MaxValueValidator(60, 'There can be no more than %(limit_value)s students in the class.'), django.core.validators.MinValueValidator(5, 'Must have at least %(limit_value)s students in class.')], verbose_name='Students limit')),
                ('monitors_limit', models.PositiveIntegerField(default=0, help_text='Monitors limit to insert in the class.', validators=[django.core.validators.MaxValueValidator(5, 'There can be no more than %(limit_value)s monitors in the class.'), django.core.validators.MinValueValidator(0, 'Ensure this value is greater than or equal to %(limit_value)s.')], verbose_name='Monitors limit')),
                ('is_closed', models.BooleanField(default=False, help_text='Close discipline.', verbose_name='Is closed?')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date that the discipline is created.', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date that the discipline is updated.', verbose_name='Updated at')),
                ('monitors', models.ManyToManyField(blank=True, related_name='monitor_classes', to=settings.AUTH_USER_MODEL, verbose_name='Monitors')),
                ('students', models.ManyToManyField(blank=True, related_name='student_classes', to=settings.AUTH_USER_MODEL, verbose_name='Students')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplines', related_query_name='discipline', to=settings.AUTH_USER_MODEL, verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Disciplines',
                'ordering': ['title', 'created_at'],
            },
        ),
    ]