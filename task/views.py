from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from project.models import Project
from .models import Comment
from .serializers import CommentSerializer
from task.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter tasks by project_id if provided
        project_id = self.kwargs.get('project_id')
        if project_id:
            return Task.objects.filter(project_id=project_id)
        return super().get_queryset()

    @action(detail=False, methods=['get', 'post'], url_path=r'(?P<project_id>\d+)/tasks')
    def project_tasks(self, request, project_id=None):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response(
                {'detail': 'Project not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'GET':
            tasks = self.get_queryset()
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        # Filter comments by task_id if provided
        task_id = self.kwargs.get('task_id')
        if task_id:
            return Comment.objects.filter(task_id=task_id)
        return super().get_queryset()

    @action(detail=False, methods=['get', 'post'], url_path=r'(?P<task_id>\d+)/comments')
    def task_comments(self, request, task_id=None):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(
                {'detail': 'Task not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'GET':
            comments = self.get_queryset()
            serializer = self.get_serializer(comments, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(task=task, user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
