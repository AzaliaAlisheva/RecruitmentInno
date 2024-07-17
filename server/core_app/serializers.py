from rest_framework import serializers
from .models import Specialists, Vacancies, User, ConnectVacanciesWithSpecialists
class SpecialistSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Specialists
        fields= '__all__'


class VacancySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Vacancies
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectVacanciesWithSpecialists
        fields = '__all__'