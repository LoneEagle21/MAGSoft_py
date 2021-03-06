# Generated by Django 2.0.1 on 2018-02-24 22:25

import re
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


def move_dob_old_to_new(apps, schema_editor):
    Users = apps.get_model('magsoft_api', 'Users')
    for user in Users.objects.all():
        user.dob = re.sub(r'(\d\d)/(\d\d)/(\d\d\d\d)',
                          r'\3-\1-\2',
                          user.dob)
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('magsoft_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='badges',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
        migrations.AlterField(
            model_name='roominfo',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
        migrations.AlterField(
            model_name='roommates',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
        migrations.AlterField(
            model_name='tab',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
        migrations.RunPython(move_dob_old_to_new),
        migrations.AlterField(
            model_name='users',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='emergencyphone',
            field=models.CharField(db_column='emergencyPhone', max_length=31, validators=[django.core.validators.RegexValidator(regex='^[-+0-9]{10,}$')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=31, validators=[django.core.validators.RegexValidator(regex='^[-+0-9]{10,}$')]),
        ),
    ]
