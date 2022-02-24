from django.contrib import admin

# Register your models here.
from .models import Image, Video, Contact

admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Contact)