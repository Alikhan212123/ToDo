from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from apps.todo.models import Task
from .permissions import TodoPermissions
from .serializers import TodoSerializers
from apps.todo.serializers import TaskSerializer
from rest_framework.response import Response

# Create your views here.
class TodoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (TodoPermissions,)

