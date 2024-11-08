from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('practices/', views.practice_list, name='practice_list'),
    path('practices/<int:pk>/register/', views.register_practice, name='register_practice'),
]
