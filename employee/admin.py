from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from employee.models import Employee, Position

admin.site.register(Position)
admin.site.register(Employee, MPTTModelAdmin)
