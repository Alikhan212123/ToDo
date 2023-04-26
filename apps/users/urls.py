from django.urls import path

from apps.users.views import UserAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register('users', UserAPIViewSet,basename="user_api" )

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name="api_login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="api_refresh")
]
urlpatterns += router.urls
