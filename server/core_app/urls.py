from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'vacancies', views.VacanciesViewSet)
router.register(r'specialists', views.SpecialistsViewSet)
router.register(r'connect',views.ConnectVacanciesWithSpecialistsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('update-specmark/', update_specmark, name='update_specmark'),
    # path('get-specmark/', get_specmark, name='get_specmark'),
]