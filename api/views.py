
# from .models import Student
# import io
# from rest_framework.parsers import JSONParser
# from .serializer import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student

@api_view(['GET' ,'POST' , 'PUT' , 'DELETE'])
def student_api(request):

    if request.method == 'GET':
        id = request.data.get('id')

        if id is not None:
            stu_model_data = Student.objects.get(id = id)
            serializer = StudentSerializer(stu_model_data)
            return Response(serializer.data)

        stu_model_data = Student.objects.all()
        serializer = StudentSerializer(stu_model_data , many = True)
        return Response(serializer.data)    

    if request.method == 'POST':
        serializer = StudentSerializer(data =  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data created"})
        return Response(serializer.errors)

    if request.method == 'PUT':

        stu_object = Student.objects.get(pk = request.data.get("id"))
        serializer = StudentSerializer(stu_object , data = request.data , partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Updated"})    
        return Response(serializer.errors)

    if request.method == 'delete':
        stu_object = Student.objects.get(pk = request.data.get('id'))
        stu_object.delete()
        return Response({'msg':"Data deleted"})
    

































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