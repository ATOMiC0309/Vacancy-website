from django.contrib import admin
from .models import Direction, Vacancy
# Register your models here.


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created', 'updated', 'published')
    list_editable = ('published', )
    list_display_links = ('pk', 'title')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'direction', 'company_name', 'work_experience_from', 'work_experience_to', 'about_company',
                    'required_task', 'convenience', 'skills', 'created', 'updated', 'published')
    list_display_links = ('pk', 'title')
    list_editable = ('published', )


admin.site.register(Direction, DirectionAdmin)
admin.site.register(Vacancy, VacancyAdmin)
