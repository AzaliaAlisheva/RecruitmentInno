from rest_framework import  viewsets
from .serializers import SpecialistSerializer, VacancySerializer, ConnectSerializer
from .models import Vacancies, Specialists, ConnectVacanciesWithSpecialists
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods 
from django.views.decorators.csrf import csrf_exempt

class VacanciesViewSet(viewsets.ModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacancySerializer


class SpecialistsViewSet(viewsets.ModelViewSet):
    queryset = Specialists.objects.all()
    serializer_class = SpecialistSerializer
 
class ConnectVacanciesWithSpecialistsViewSet(viewsets.ModelViewSet):
    queryset = ConnectVacanciesWithSpecialists.objects.all()
    serializer_class = ConnectSerializer
