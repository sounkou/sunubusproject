from django.contrib import admin

# Register your models here.
from . models import Heroes
admin.site.register(Heroes)
from . models import Ligne
admin.site.register(Ligne)
