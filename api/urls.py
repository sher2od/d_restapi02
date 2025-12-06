from django.urls import path
from .views import CategoryViewSet, TasksViewSet, RegisterView,LoginView


urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path('categories/', CategoryViewSet.as_view({'get':'list','post':'create'})),
    path('categories/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve', 'post':'update','delete':'destroy'})),
    path('tasks/',TasksViewSet.as_view({'get':'list','post':'create'})),
    path('tasks/<int:pk>/', TasksViewSet.as_view({'get':'retrieve', 'post':'update','delete':'destroy'}))


]

