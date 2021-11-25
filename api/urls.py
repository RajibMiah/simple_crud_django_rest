from django.urls import path
from .views import LCStudentListAPI , RUDStudentAPI
# student_api

urlpatterns = [
    path('', LCStudentListAPI.as_view()),
    path('<int:pk>/' , RUDStudentAPI.as_view())
    # path('', student_api.as_view()),
    # path('<int:pk>/',student_api.as_view())
]
