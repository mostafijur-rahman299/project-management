from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
    username = models.CharField(max_length=225, unique=True)
    first_name = models.CharField(max_length=225, null=True)
    last_name = models.CharField(max_length=225, null=True)
    email = models.EmailField(max_length=225, unique=True)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        # Always store email in lower case
        if self.email:
            self.email = self.email.lower()

        # Check case-insensitive uniqueness manually
        if User.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError("A user with this email already exists.")

        super().save(*args, **kwargs)
