from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student


@api_view(['GET'])
def apiOverview(request):
	tasks = Student.objects.all().order_by('-id')
	serializer = StudentSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def studentData(request):
    data = request.data
    student = Student.objects.get(LRN=data['lrn'])
    serializer = StudentSerializer(student)
    return Response(serializer.data)

