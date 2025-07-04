from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include('user.urls')),
    path('api/', include('project.urls')),
    path('api/', include('task.urls'))
]
