from django.contrib import admin

from .models import *


admin.site.register(Project)
admin.site.register(Sample)
admin.site.register(Screen)
admin.site.register(Well)
admin.site.register(Plate)
admin.site.register(Receptor)