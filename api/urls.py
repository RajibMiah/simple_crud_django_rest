from django.urls import path
from .views import student_api

urlpatterns = [
    path('', student_api),
    path('<int:pk>/',student_api)
]
