from django.db import models

# Create your models here.
from geo_spatial.models import District, Thana
from user.models import CustomUser


class Warrant(models.Model):
    issue_date = models.DateField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='warrants')
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, related_name='warrants')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='warrants')


class WarrantFile(models.Model):
    warrant = models.ForeignKey(Warrant, on_delete=models.CASCADE, related_name='warrant_files')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    attachment = models.FileField()
    created_time = models.DateTimeField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='warrant_files')
