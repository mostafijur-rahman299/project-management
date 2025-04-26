from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_id>/tasks/', TaskViewSet.as_view({'get': 'project_tasks', 'post': 'project_tasks'}), name='project-tasks'),
    path('tasks/<int:task_id>/comments/', CommentViewSet.as_view({'get': 'task_comments', 'post': 'task_comments'}), name='task-comments'),
]
