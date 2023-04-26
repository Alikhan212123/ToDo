from django.urls import path
from .views import TodoAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todo', TodoAPIViewSet, basename="todo_api")

urlpatterns = [

]
urlpatterns += router.urls
