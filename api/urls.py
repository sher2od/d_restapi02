from django.urls import path
from .views import CategoryViewSet, TasksViewSet

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get':'list','post':'create'})),
    path('categories/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve', 'post':'update','delete':'destroy'})),
    path('tasks/',TasksViewSet.as_view({'get':'list','post':'create'})),
    path('tasks/<int:pk>/', TasksViewSet.as_view({'get':'retrieve', 'post':'update','delete':'destroy'}))


]

