import datetime

from django.db import models
from geo_spatial.models import District, Thana, Union, PoliceUnit
from user.models import CustomUser


class Warrant(models.Model):
    entry_date = models.DateTimeField()
    issue_date = models.DateField()
    warrant_type = models.IntegerField()
    court_name = models.CharField(max_length=255)
    warrant_person_name_age = models.CharField(max_length=300)
    warrant_person_father_name = models.CharField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.RESTRICT, related_name='warrants')
    thana = models.ForeignKey(Thana, on_delete=models.RESTRICT, related_name='warrants')
    union = models.ForeignKey(Union, on_delete=models.RESTRICT, related_name='warrants')
    address = models.TextField(null=True)
    gr_cr_no = models.IntegerField()
    gr_cr_year = models.IntegerField(null=True)
    case_file_station = models.ForeignKey(Thana, on_delete=models.RESTRICT, related_name='warrants')
    concerned_police_unit = models.ForeignKey(PoliceUnit, on_delete=models.RESTRICT, related_name='warrants')
    case_type_section = models.CharField(max_length=255)
    date_of_presentation_in_court = models.DateField(null=True)
    court_process_no = models.CharField(max_length=255, null=True)
    court_given_other_info = models.TextField(null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='warrants')
    created_time = models.DateTimeField(default=datetime.datetime)


class WarrantFile(models.Model):
    warrant = models.ForeignKey(Warrant, on_delete=models.CASCADE, related_name='warrant_files')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    attachment = models.FileField()
    created_time = models.DateTimeField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='warrant_files')
