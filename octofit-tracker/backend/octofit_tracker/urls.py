from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        scheme = 'https' if request.is_secure() else 'http'
        base_url = f"{scheme}://{request.get_host()}"
    return Response({
        'users': f"{base_url}{reverse('user-list')}",
        'teams': f"{base_url}{reverse('team-list')}",
        'activities': f"{base_url}{reverse('activity-list')}",
        'leaderboard': f"{base_url}{reverse('leaderboard-list')}",
        'workouts': f"{base_url}{reverse('workout-list')}",
    })

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
