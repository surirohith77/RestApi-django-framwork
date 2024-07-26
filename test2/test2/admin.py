# from django.contrib import admin
# from .models import Cricketers
#
# # Register your models here.
#
# admin.site.register(Cricketers)
#

from django.contrib import admin
from .models import Cricketers, UploadedFile


class CricketersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')


# Register each model with its respective ModelAdmin
admin.site.register(Cricketers, CricketersAdmin)
admin.site.register(UploadedFile, UploadedFileAdmin)
