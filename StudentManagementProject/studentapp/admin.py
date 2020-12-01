from django.contrib import admin
from .models import Register, Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'marks_inter', 'is_selected']
    ordering = ['marks_inter']
    list_editable = ['is_selected']


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'department']
    ordering = ['id']


admin.site.register(Register, RegisterAdmin)
admin.site.register(Application, ApplicationAdmin)
