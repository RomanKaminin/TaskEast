from django.contrib import admin
from .models import Department, Client
from mptt.admin import MPTTModelAdmin

class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']


class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','position', 'start_work_date', 'end_work_date', 'department')
    list_filter = ['department','end_work_date']
    search_fields = ['username', 'first_name']


    def start_work_date(self, obj):
        return obj.start_work_date

admin.site.register(Client, ClientAdmin)
admin.site.register(Department, DepartmentAdmin)
