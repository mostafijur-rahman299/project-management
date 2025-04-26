from rest_framework import serializers
from .models import Task, Comment
from user.models import User


class TaskSerializer(serializers.ModelSerializer):
    assigned_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'assigned_to', 'assigned_user', 'created_at', 'due_date'
        ]
        read_only_fields = ['created_at']
        extra_kwargs = {
            'assigned_to': {'required': True, "write_only": True},
            'title': {'required': True},
            'description': {'required': False},
            'status': {'required': True},
            'priority': {'required': True},
            'due_date': {'required': True},
        }
        
    def get_assigned_user(self, obj):
        if obj.assigned_to:
            return {
                'id': obj.assigned_to.id,
                'username': obj.assigned_to.username,
                'email': obj.assigned_to.email
            }
        return None


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']
        
    def get_user(self, obj):
        if obj.user:
            return {
                'id': obj.user.id,
                'username': obj.user.username,
                'email': obj.user.email
            }
        return None
        