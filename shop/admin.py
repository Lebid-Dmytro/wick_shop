from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Wick, User


@admin.register(Wick)
class WickAdmin(ModelAdmin):
    pass


@admin.register(User)
class WickAdmin(ModelAdmin):
    pass
