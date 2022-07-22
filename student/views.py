import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from . import models
from .models import Students
from .serializers import StudentSerializers, PatchStudentSerializer


# Create your views here.


def student(request):
    if request.method == "GET":
        data = Students.objects.all()
        serializer = StudentSerializers(instance=data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        try:
            serializer = StudentSerializers(data=data)
            serializer.is_valid(raise_exception=True)
        except:
            return JsonResponse(serializer.errors, status=422)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


def student_id(request, pk):
    if request.method == "GET":
        try:
            data = Students.objects.get(id=pk)
        except models.Students.DoesNotExist:
            return JsonResponse({"error_message": "学生ID不存在"})
        serializer = StudentSerializers(instance=data)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        try:
            request_body = json.loads(request.body)
            data = Students.objects.get(id=pk)
        except models.Students.DoesNotExist:
            return JsonResponse({"error_message": "学生ID不存在"})
        serializer = StudentSerializers(instance=data, data=request_body)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return JsonResponse(serializer.errors, status=422)
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    elif request.method == "PATCH":
        try:
            student_obj = Students.objects.get(id=pk)
        except models.Students.DoesNotExist:
            return JsonResponse({"error_message": "学生ID不存在"})
        new_student_data = json.loads(request.body)
        serializer = PatchStudentSerializer(data=new_student_data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return JsonResponse(serializer.errors, status=422)
        for key, value in new_student_data.items():
            if key == "name":
                student_obj.name = value
            elif key == "age":
                student_obj.age = value
            elif key == "cls":
                student_obj.cls = value
            elif key == "score":
                student_obj.score = value
            elif key == "remake":
                student_obj.remake = value
            else:
                continue
        student_obj.save()

        serializer_2 = StudentSerializers(instance=student_obj)
        return JsonResponse(serializer_2.data, status=201)
    elif request.method == "DELETE":
        try:
            student_obj = Students.objects.get(id=pk)
        except models.Students.DoesNotExist:
            return JsonResponse({"error_message": "学生ID不存在"})
        student_obj.delete()
        return JsonResponse({"msg": "删除成功"}, status=204)
