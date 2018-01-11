from django.contrib import admin

from app.Newsapp.models import New, Description

# Register your models here.


admin.site.register(New)
admin.site.register(Description)
