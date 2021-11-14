import datetime

from django.db import models
from geo_spatial.models import District, Thana, Union, PoliceUnit
from user.models import CustomUser


class Warrant(models.Model):
    entry_date = models.DateField()
    issue_date = models.DateField()
    WARRANT_TYPE_CHOICE = (
        (1, 'GR'),
        (2, 'GR Punishment'),
        (3, 'CR'),
        (4, 'CR Punishment'),
        (5, 'Others'),
    )
    warrant_type = models.IntegerField(choices=WARRANT_TYPE_CHOICE)
    court_name = models.CharField(max_length=255, )
    warrant_person_name_age = models.CharField(max_length=300)
    warrant_person_father_name = models.CharField(max_length=300, blank=True)
    district = models.ForeignKey(District, on_delete=models.RESTRICT, related_name='warrants')
    thana = models.ForeignKey(Thana, on_delete=models.RESTRICT, related_name='warrants')
    union = models.ForeignKey(Union, on_delete=models.RESTRICT, related_name='warrants', blank=True)
    address = models.TextField(null=True, blank=True)
    gr_cr_no = models.IntegerField(default=None, )
    gr_cr_year = models.PositiveSmallIntegerField(null=True, blank=True)
    case_file_station = models.ForeignKey(Thana, default=None, on_delete=models.RESTRICT,
                                          related_name='warrants_station')
    concerned_police_unit = models.ForeignKey(PoliceUnit, default=None, on_delete=models.RESTRICT,
                                              related_name='warrants', blank=True, null=True)
    case_type_section = models.CharField(max_length=255, default=None, blank=True)
    date_of_presentation_in_court = models.DateField(null=True, default=None, blank=True)
    court_process_no = models.CharField(max_length=255, null=True, blank=True)
    court_given_other_info = models.TextField(null=True, blank=True)
    SETTLEMENT_TYPE_CHOICE = (
        (1, 'OTHERS'),
        (2, 'NIR SUBMISSION'),
        (3, 'TAMIL'),
        (4, 'RECALL')
    )
    warrant_settlement_type = models.PositiveSmallIntegerField(null=True, choices=SETTLEMENT_TYPE_CHOICE)
    warrant_settlement_date = models.DateField(default=None, null=True)
    tamil_settlement_date = models.DateField(default=None, null=True)
    tamil_officer_info = models.TextField(default=None, null=True, max_length=255)
    tamil_officer_bp_no = models.TextField(default=None, null=True, max_length=255)
    APPROVE_STATUS_CHOICE = (
        (1, 'Pending'),
        (2, 'Approved'),
    )
    approve_status = models.PositiveSmallIntegerField(default=1, choices=APPROVE_STATUS_CHOICE)
    picture = models.ImageField(upload_to='warrant/picture/', default=None, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='warrants', null=True,
                                   blank=True, default=None)
    created_time = models.DateTimeField(null=True, default=None)


class WarrantFile(models.Model):
    warrant = models.ForeignKey(Warrant, on_delete=models.CASCADE, related_name='warrant_files')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    attachment = models.FileField(upload_to="warrant/files/%Y/%m/%d")
    created_time = models.DateTimeField(null=True, default=None)
    created_by = models.ForeignKey(CustomUser, null=True, default=None, on_delete=models.CASCADE, related_name='warrant_files')


