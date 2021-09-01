# Generated by Django 3.2.5 on 2021-08-31 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geo_spatial', '0005_auto_20210831_2041'),
        ('warrant', '0003_auto_20210831_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrant',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='case_type_section',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='concerned_police_unit',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='warrants', to='geo_spatial.policeunit'),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='court_given_other_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='court_process_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='warrants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='date_of_presentation_in_court',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='gr_cr_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='union',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='warrants', to='geo_spatial.union'),
        ),
        migrations.AlterField(
            model_name='warrant',
            name='warrant_person_father_name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]