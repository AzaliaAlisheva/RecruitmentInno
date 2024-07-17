from django.urls import include, path
from rest_framework import routers
# from .views import update_specmark, get_specmark
from . import views

router = routers.DefaultRouter()
router.register(r'vacancies', views.VacanciesViewSet)
router.register(r'specialists', views.SpecialistsViewSet)
router.register(r'users', views.UsersViewSet)
router.register(r'connect',views.ConnectVacanciesWithSpecialistsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('update-specmark/', update_specmark, name='update_specmark'),
    # path('get-specmark/', get_specmark, name='get_specmark'),
]