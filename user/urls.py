from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('users/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
]
