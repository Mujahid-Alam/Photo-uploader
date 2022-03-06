from django.contrib import admin
from .models import Photos
# Register your models here.
@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id','title','descriptions','images']