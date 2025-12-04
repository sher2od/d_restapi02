from rest_framework.viewsets import ModelViewSet
from .models import Category,Task
from .serializers import CategorySerializer, TaskSerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TasksViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()