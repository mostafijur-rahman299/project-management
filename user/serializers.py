from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'date_joined']
        read_only_fields = ['date_joined']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'required': True, 'write_only': True},
        }
        
    def validate_email(self, email):
        """
        Validate the email field to ensure it is unique.
        """
        
        # Check if the email is being updated and is the same as the current instance's email
        if self.instance and self.instance.email == email:
            return email
        
        # Check if the email already exists in the database
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email already exists.")
        return email
    
    def validate_username(self, username):
        """
        Validate the username field to ensure it is unique.
        """
        
        # Check if the username is being updated and is the same as the current instance's username
        if self.instance and self.instance.username == username:
            return username
        
        # Check if the username already exists in the database
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("Username already exists.")
        return username
    
    def create(self, validated_data):
        """
        Create a new user instance with the validated data.
        """
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        """
        Update the user instance with the validated data.
        """
        
        # Update the fields of the instance with the validated data
        for field in validated_data:
            if field in ['username', 'email', 'first_name', 'last_name']:
                setattr(instance, field, validated_data[field])
                
        # Check if the password is being updated
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            
        # Save the instance
        instance.save()
        return instance
