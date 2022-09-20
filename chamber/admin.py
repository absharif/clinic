from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('name', 'phone', 'district')


class PrescriptionAdmin(ImportExportModelAdmin):
    list_display = ('profile', 'created_by')


class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('name',)


class BookAdmin(ImportExportModelAdmin):
    list_display = ('name',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(BookNo, BookAdmin)
