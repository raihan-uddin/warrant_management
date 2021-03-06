# Generated by Django 3.2.5 on 2021-08-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_spatial', '0004_alter_union_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policeunit',
            name='status',
            field=models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True),
        ),
        migrations.AlterField(
            model_name='thana',
            name='status',
            field=models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True),
        ),
    ]
