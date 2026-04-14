from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, StudentViewSet


# Create router
router = DefaultRouter()
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'students', StudentViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
]