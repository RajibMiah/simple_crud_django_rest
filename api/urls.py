from django.urls import path , include
from .views import StudentModelSet ,StudentModelRonlyViewSet
from rest_framework.routers import DefaultRouter
# student_api

router = DefaultRouter()

router.register('studentapi' , StudentModelRonlyViewSet , basename='student')

urlpatterns = [
    path('', include(router.urls))
    # path('', StudentModelSet.as_view()),
    # path('<int:pk>/' , StudentModelSet.as_view())
    # path('', student_api.as_view()),
    # path('<int:pk>/',student_api.as_view())
]
