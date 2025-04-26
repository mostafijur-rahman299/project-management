from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include('user.urls')),
    # path('api/', include('projects.urls')),
    # path('api/', include('tasks.urls')),
    # path('api/', include('comments.urls')),
]
