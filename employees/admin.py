from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    # Columns displayed in admin panel
    list_display = (
        'id',
        'name',
        'age',
        'email',
        'phone',
        'department',
        'salary',
        'joining_date',
    )

    # Search employees
    search_fields = ('name', 'email', 'department')

    # Filter employees
    list_filter = ('department', 'joining_date')

    # Default ordering
    ordering = ('id',)
