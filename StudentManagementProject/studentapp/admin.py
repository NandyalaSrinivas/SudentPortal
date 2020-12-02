from django.contrib import admin
from .models import Register, Application
from django.contrib.admin import SimpleListFilter


class Selected(admin.SimpleListFilter):
    title = ('is_selected')
    parameter_name = 'selected'

    def lookups(self, request, model_admin):
        return (
            ('True','selected',),
            ('False','unselected'),
        )


    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(marks_inter__gte=900)

        if self.value() == 'False':
            return queryset.filter(marks_inter__lte=900)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'marks_inter', 'is_selected']
    ordering = ['marks_inter']
    list_editable = ['is_selected', 'Selected']


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'department']
    ordering = ['id']


admin.site.register(Register, RegisterAdmin)
admin.site.register(Application, ApplicationAdmin)
