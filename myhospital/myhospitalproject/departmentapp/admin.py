from django.contrib import admin
from .models import Doctor, Department


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, DepartmentAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','roomno', 'available', 'created', 'updated']
    list_editable = ['roomno', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Doctor, DoctorAdmin)
