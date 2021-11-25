from django.urls import path
from .views import student_api

urlpatterns = [
    path('', student_api.as_view()),
    path('<int:pk>/',student_api.as_view())
]
