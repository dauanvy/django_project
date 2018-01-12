from django.contrib import admin

# Register your models here.
from home.models import Category
from home.models import Location
from home.models import Events

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Events)