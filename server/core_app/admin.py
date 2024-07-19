from django.contrib import admin
from .models import Vacancies, Specialists, ConnectVacanciesWithSpecialists

admin.site.register(Vacancies)
admin.site.register(Specialists)
admin.site.register(ConnectVacanciesWithSpecialists)