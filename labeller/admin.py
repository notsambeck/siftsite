from django.contrib import admin

from .models import Image, Choice, TotalVotes

admin.site.register(Image)
admin.site.register(Choice)
admin.site.register(TotalVotes)
# Register your models here.
