from django.contrib import admin

from .models import Image, UserLabel, TotalVotes

admin.site.register(Image)
admin.site.register(UserLabel)
admin.site.register(TotalVotes)
# Register your models here.
