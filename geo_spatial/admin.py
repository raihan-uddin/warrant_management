from django.contrib import admin

# Register your models here.
from geo_spatial.models import District, Thana, Union

admin.site.register(District)
admin.site.register(Thana)
admin.site.register(Union)
