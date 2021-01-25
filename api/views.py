from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer, SHStudentSerializer
from .models import JuniorHigh, SeniorHigh


@api_view(['GET'])
def apiOverview(request):
	tasks = JuniorHigh.objects.all().order_by('-id')
	serializer = StudentSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def studentData(request):
    data = request.data
    student = JuniorHigh.objects.get(LRN=data['lrn'])
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(['POST'])
def studentPush(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def shapiOverview(request):
	tasks = SeniorHigh.objects.all().order_by('-id')
	serializer = SHStudentSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def shstudentData(request):
    data = request.data
    student = SeniorHigh.objects.get(LRN=data['lrn'])
    serializer = SHStudentSerializer(student)
    return Response(serializer.data)