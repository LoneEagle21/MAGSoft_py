# Generated by Django 2.0.1 on 2018-03-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsoft_api', '0002_auto_20180224_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badges',
            old_name='badgedata',
            new_name='badge_data',
        ),
        migrations.RenameField(
            model_name='badges',
            old_name='badgename',
            new_name='badge_name',
        ),
        migrations.RenameField(
            model_name='badges',
            old_name='badgeadded',
            new_name='badge_added',
        ),
        migrations.AlterField(
            model_name='badges',
            name='badge_added',
            field=models.BooleanField(db_column='badgeAdded', default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='badges',
            name='spam',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='roommates',
            name='parties',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='roommates',
            name='wantstoroom',
            field=models.BooleanField(db_column='wantsToRoom'),
        ),
        migrations.AlterField(
            model_name='tab',
            name='housecharge',
            field=models.BooleanField(db_column='houseCharge'),
        ),
    ]
