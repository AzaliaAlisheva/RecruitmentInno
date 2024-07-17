from django.contrib import admin
from .models import Vacancies, Specialists, ConnectVacanciesWithSpecialists, User

admin.site.register(Vacancies)
admin.site.register(Specialists)
admin.site.register(ConnectVacanciesWithSpecialists)
admin.site.register(User)