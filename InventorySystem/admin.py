from django.contrib import admin
from .models import User, User_Admin, Hire_Reference, Hardware, NonElectronic_Hardware, Electronic_Hardware

admin.site.register(User)
admin.site.register(User_Admin)
admin.site.register(Hire_Reference)
admin.site.register(Hardware)
admin.site.register(NonElectronic_Hardware)
admin.site.register(Electronic_Hardware)
