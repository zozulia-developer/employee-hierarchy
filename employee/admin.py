from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from employee.models import Employee, Position


class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_per_page = 10


class EmployeeDraggableMPTTAdmin(DraggableMPTTAdmin):
    list_display = [
        'first_name',
        'last_name',
        'middle_name',
        'position',
        'email',
        'hire_date',
        'parent',
    ]
    list_display_links = ['first_name']
    list_per_page = 10
    mptt_level_indent = 10


admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeDraggableMPTTAdmin)
