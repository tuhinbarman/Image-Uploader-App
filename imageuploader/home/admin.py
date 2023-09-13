from django.contrib import admin

from .models import Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','name','about','photo','datetime')

    list_display_links = ('id','name','photo')
    list_editable = ('about',)
    list_per_page = 10

admin.site.register(Image,ImageAdmin)
