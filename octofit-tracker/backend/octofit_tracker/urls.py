"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import os
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardEntryViewSet
from django.http import JsonResponse

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    if codespace_name == 'localhost':
        base_url = 'http://localhost:8000/api/'
    else:
        base_url = f'https://{codespace_name}-8000.app.github.dev/api/'
    return JsonResponse({
        "activities": f"{base_url}activities/",
        "workouts": f"{base_url}workouts/",
        "teams": f"{base_url}teams/",
        "users": f"{base_url}users/",
        "leaderboard": f"{base_url}leaderboard/"
    })


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
