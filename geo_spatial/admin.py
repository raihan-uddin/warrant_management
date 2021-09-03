from django.contrib import admin

# Register your models here.
from geo_spatial.models import District, Thana, Union, PoliceUnit


class DistrictAdvanceFilter(admin.ModelAdmin):
    # list_filter = [
    #     "name",
    #     "name_bn",
    #     "code",
    #     "status"
    # ]
    search_fields = [
        "name",
        "name_bn",
        "status",
        "code",
    ]
    list_display = ('name', 'name_bn', 'code', 'status')
    # list_display_links = ('name',)
    list_filter = ('name', 'name_bn', 'code')
    list_per_page = 10


admin.site.register(District, DistrictAdvanceFilter)
admin.site.register(Thana)
admin.site.register(Union)
admin.site.register(PoliceUnit)
