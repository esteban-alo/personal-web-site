from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['created_date', 'update_date']  # Show 'created_date', 'update_date' in admin


admin.site.register(Project, ProjectAdmin)


