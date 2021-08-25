from django.db import models


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    status = models.BooleanField(default=True)


class Thana(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='thanas')
    name_bn = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    status = models.BooleanField(default=True)


class Union(models.Model):
    name = models.CharField(max_length=255)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, related_name='unions')
    name_bn = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
