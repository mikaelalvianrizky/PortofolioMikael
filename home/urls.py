from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('project_details/<int:project_id>/', views.project_details, name='project_details'),
    path('MachineLearning_Project', views.ml_project, name='ml_project'),
    path('WebDeveloper_Project', views.webdev_project, name='webdev_project'),
    path('AppDev_Project', views.app_project, name='appdev_project'),
]