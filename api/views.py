
# from .models import Student
# import io
# from rest_framework.parsers import JSONParser
# from .serializer import StudentSerializer
# from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET' ,'POST'])
def student_api(request):

    if request.method == 'GET':
        return Response({'msg':'This is get  request'})

    if request.method == 'POST':
        print('request', request.data)
        return Response({'msg':'This is post request'} , "data" , request.data)
    


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