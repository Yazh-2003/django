from django.shortcuts import render
from .models import studentModel
from django.http import JsonResponse
# Create your views here.

def studentView(request):
    student = studentModel.objects.all()
    student_list =list(student.values())
    return JsonResponse(student_list, safe=False)
