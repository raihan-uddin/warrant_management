from django.db import models


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Thana(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.RESTRICT, related_name='thanas')
    name_bn = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=True)


class Union(models.Model):
    name = models.CharField(max_length=255)
    thana = models.ForeignKey(Thana, on_delete=models.RESTRICT, related_name='unions')
    name_bn = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=True)


class PoliceUnit(models.Model):
    name = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, null=True)
    contact_no = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    remarks = models.TextField(max_length=255, null=True)
    status = models.BooleanField(default=True)
