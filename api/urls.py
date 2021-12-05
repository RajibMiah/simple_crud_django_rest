from django.urls import path , include
from .views import StudentModelRonlyViewSet , StudentList
from rest_framework.routers import DefaultRouter
# student_api

router = DefaultRouter()

router.register('studentapi' , StudentModelRonlyViewSet , basename='student')
# router.register('stu-filter',StudentList , basename= 'student')
urlpatterns = [
    path('', include(router.urls)),
    path('stu-filter/',StudentList.as_view())
    # path('', StudentModelSet.as_view()),
    # path('<int:pk>/' , StudentModelSet.as_view())
    # path('', student_api.as_view()),
    # path('<int:pk>/',student_api.as_view())
]
