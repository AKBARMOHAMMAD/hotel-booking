from django.contrib import admin
from .models import Hotels
from .models import Room
from .models import Review

# Register your models here.
admin.site.register(Hotels)
admin.site.register(Room)
admin.site.register(Review)