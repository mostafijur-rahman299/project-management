from rest_framework import serializers
from .models import Task
from user.models import User
from project.models import Project


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

        