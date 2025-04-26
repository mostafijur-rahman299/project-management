from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_id>/tasks/', TaskViewSet.as_view({'get': 'project_tasks', 'post': 'project_tasks'}), name='project-tasks'),
]
