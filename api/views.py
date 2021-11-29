
# from .models import Student
# import io
# from rest_framework.parsers import JSONParser
# from .serializer import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from django.views.decorators.csrf import csrf_exempt

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializer import StudentSerializer
# from .models import Student

# from rest_framework.views import APIView
# from rest_framework.response import Response


# from rest_framework import  status
# from .serializer import StudentSerializer
# from .models import Student
# from rest_framework.mixins  import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin
# from rest_framework.generics import GenericAPIView

# from .serializer import StudentSerializer
# from .models import Student
# from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

from rest_framework.authentication import BasicAuthentication ,SessionAuthentication
from rest_framework.permissions import IsAuthenticated ,AllowAny, IsAuthenticatedOrReadOnly

from .serializer import StudentSerializer
from .models import Student
from rest_framework import  viewsets


#<--------- model view sets ------------>

class StudentModelSet(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
    
    authentication_classes = [BasicAuthentication]
    permission_classes =  [AllowAny]

    

    


class StudentModelRonlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
    
    authentication_classes = [SessionAuthentication]
    permission_classes =  [IsAuthenticated]

    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermission]













#<----------concrete view --------------->



# class StudentListCreateAPI(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

















#<---------------create model mixin -------------->

# class LCStudentListAPI(GenericAPIView , ListModelMixin , CreateModelMixin):

#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self , request , *args , **kwargs):
#         return self.list(request , *args , **kwargs)

#     def post(self , request ,*args , **kwargs):
#         return self.create(request , *args , **kwargs)

# class RUDStudentAPI(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request , *args , **kwargs):
#         return self.retrieve(request , *args , **kwargs)

#     def put(self , request , *args, **kwargs):
#         return self.update(request, *args ,**kwargs)

#     def delete(self , request , *args , **kwargs):
#         return self.destroy(request , *args , **kwargs)        












# <-------------class based api view ------------>

# class student_api(APIView):

#     def get(self  , pk = None , format = None):
#         id = pk
#         if id is not None:
#             stu_model_data = Student.objects.get(id = pk)
#             serializer = StudentSerializer(stu_model_data)
#             return Response(serializer.data)

#         stu_model_data = Student.objects.all()
#         serializer = StudentSerializer(stu_model_data , many = True)
#         return Response(serializer.data)

#     def post(self , request , format = None ):
#         serializer = StudentSerializer(data =  request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Data created"} ,status  = status.HTTP_201_CREATED)
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
#     def put(self , request , pk = None , format =  None):
#         stu_object = Student.objects.get(pk = pk)
#         serializer = StudentSerializer(stu_object , data = request.data , )

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Complete data Updated"} , status= status.HTTP_200_OK)    
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
#     def patch(self , request , pk = None , format = None):
#         stu_object = Student.objects.get(pk = pk)
#         serializer = StudentSerializer(stu_object , data = request.data , partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Parital data Updated"})    
#         return Response(serializer.errors , status=  status.HTTP_400_BAD_REQUEST)    

#     def delete(self , pk = None , format = None):
#         stu_object = Student.objects.get(pk = pk)
#         stu_object.delete()
#         return Response({'msg':"Data deleted"} , status = status.HTTP_200_OK)






























# <--------function view api view ----------------->


# @api_view(['GET' ,'POST' , 'PUT' , 'PATCH','DELETE'])
# def student_api(request , pk = None):

#     if request.method == 'GET':

#         id = pk
#         if id is not None:
#             stu_model_data = Student.objects.get(id = pk)
#             serializer = StudentSerializer(stu_model_data)
#             return Response(serializer.data)

#         stu_model_data = Student.objects.all()
#         serializer = StudentSerializer(stu_model_data , many = True)
#         return Response(serializer.data)    

#     if request.method == 'POST':
#         serializer = StudentSerializer(data =  request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Data created"} ,status  = status.HTTP_201_CREATED)
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT':

#         stu_object = Student.objects.get(pk = pk)
#         serializer = StudentSerializer(stu_object , data = request.data , )

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Complete data Updated"} , status= status.HTTP_200_OK)    
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PATCH':

#         stu_object = Student.objects.get(pk = pk)
#         serializer = StudentSerializer(stu_object , data = request.data , partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Parital data Updated"})    
#         return Response(serializer.errors , status=  status.HTTP_400_BAD_REQUEST)    

#     if request.method == 'delete':
#         stu_object = Student.objects.get(pk = pk)
#         stu_object.delete()
#         return Response({'msg':"Data deleted"} , status = status.HTTP_200_OK)
    

































# @csrf_exempt
# def student_api(request):

#     if request.method =='GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         complex_data = JSONParser().parse(stream)
#         id = complex_data.get('id' , None)

#         if id is not None:
#             student_data  = Student.objects.get(id = id)
#             serializer = StudentSerializer(student_data)
#         else:
#             all_student_data  = Student.objects.all()
#             serializer = StudentSerializer(all_student_data , many = True)

#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data , content_type = 'application/json')    

#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         complex_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = complex_data)
        
#         if serializer.is_valid():
#             serializer.save()
#             res = {"res":"Data created !!"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data , content_type = 'application/json')

#         json_data =  JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data , content_type = 'application/json')

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         complex_data = JSONParser().parse(stream)
#         id = complex_data.get('id')
#         stu = Student.objects.get( id = id)
#         serializer = StudentSerializer(stu , data = complex_data , partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'res':' Data updated !! '}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data , content_type = 'application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data , content_type = 'application/json')    