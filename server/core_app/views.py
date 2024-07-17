from rest_framework import  viewsets
from .serializers import SpecialistSerializer, VacancySerializer, UserSerializer, ConnectSerializer
from .models import Vacancies, Specialists, User, ConnectVacanciesWithSpecialists
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

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@require_http_methods(["POST"])
def update_specmark(request):
    vacancy_id = request.POST.get('vacancy_id')
    specialist_id = request.POST.get('specialist_id')
    new_specmark = request.POST.get('specmark')

    if not (vacancy_id and specialist_id and new_specmark):
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    connect_entry = get_object_or_404(ConnectVacanciesWithSpecialists, vacancy_id=vacancy_id, specialist_id=specialist_id)
    connect_entry.specmark = new_specmark
    connect_entry.save()

    return JsonResponse({'success': True})

@csrf_exempt
def get_specmark(request):
    if request.method == 'GET':
        vacancy_id = request.GET.get('vacancy_id')
        specialist_id = request.GET.get('specialist_id')
        
        try:
            connection = ConnectVacanciesWithSpecialists.objects.get(vacancy_id=vacancy_id, specialist_id=specialist_id)
            return connection.specmark
        except ConnectVacanciesWithSpecialists.DoesNotExist:
            return False

    return False

class ConnectVacanciesWithSpecialistsViewSet(viewsets.ModelViewSet):
    queryset = ConnectVacanciesWithSpecialists.objects.all()
    serializer_class = ConnectSerializer
