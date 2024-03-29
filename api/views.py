
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer, SHStudentSerializer, AllStatus
from .models import JuniorHigh, SecondQuarter, SeniorHigh, Status, FirstQuarter, ThirdQuarter


@api_view(['GET'])
def apiOverview(request):
	tasks = JuniorHigh.objects.all().order_by('-id')
	serializer = StudentSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def allstatus(request):
	tasks = Status.objects.all().order_by('-id')
	serializer = AllStatus(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def studentData(request):
    #{Name, Teacher, Student_id, LRN, Section, Quarter, data:[{subject, grade}], data2: [{subject, grade}]}
    data = request.data
    print(data)
    student = JuniorHigh(Name=data['Name'], Teacher=data['Teacher'], Student_id=data['Student_id'],
    LRN=data['LRN'], Status=True, Section=data['Section'], Quarter='1')
    student.save()
    for i in (data['data']):
        first = FirstQuarter(Subject=i['Subject'], Grade=i['Grade'], Student=student)
        first.save()
        print(i)
    for i in (data['data2']):
        first = SecondQuarter(Subject=i['Subject'], Grade=i['Grade'], Student=student)
        first.save()
        print(i)
    for i in (data['data3']):
        first = ThirdQuarter(Subject=i['Subject'], Grade=i['Grade'], Student=student)
        first.save()
        print(i)
    serializer = StudentSerializer(student)
    studentdata = serializer.data
    return Response(studentdata)

@api_view(['POST']) 
def real_api(request):
    #{'lrn':lrn, 'level': seniorhigh or juniorhigh, 'student_id': student_id}
    data = request.data
    print(data['lrn'])
    if data['level'] == 'SeniorHigh':
        try:
            student = SeniorHigh.objects.get(LRN=data['lrn'])
        except:
            return JsonResponse({'message': 'wrong entry for student id'})
        serializer = SHStudentSerializer(student)
        studentdata = serializer.data
        if data['student_id'] == studentdata['Student_id']:
            firstgrade = studentdata['firstgrade']
            secondgrade = studentdata['secondgrade']
            head = {'level': 1,'Name': studentdata['Name'], 'LRN': studentdata['LRN'], 'Teacher': studentdata['Teacher'], 'Status': studentdata['Status'], 'Section': studentdata['Section']}
            grade = []
            head['data'] = grade
            for i in range(len(firstgrade)):
                final = (float(firstgrade[i]['Grade']) + float(secondgrade[i]['Grade']))/ 2
                data = {'Subject': firstgrade[i]['Subject'], 'Data':[firstgrade[i]['Grade'], secondgrade[i]['Grade']]}
                grade.append(data)
            return JsonResponse(head)
        else:
            return JsonResponse({'message': 'wrong entry for student id'})

        return Response(serializer.data)
    elif data['level'] == 'JuniorHigh':
        try:
            student = JuniorHigh.objects.get(LRN=data['lrn'])
        except:
            return JsonResponse({'message': 'wrong entry for student id'})
        serializer = StudentSerializer(student)
        studentdata = serializer.data
        if data['student_id'] == studentdata['Student_id']:
            firstgrade = studentdata['firstgrade']
            secondgrade = studentdata['secondgrade']
            thirdgrade = studentdata['thirdgrade']
            head = {'level': 0, 'Name': studentdata['Name'], 'LRN': studentdata['LRN'], 'Teacher': studentdata['Teacher'], 'Status': studentdata['Status'], 'Section': studentdata['Section']}
            grade = []
            head['data'] = grade
            for i in range(len(firstgrade)):
                data = {'Subject': firstgrade[i]['Subject'], 'Data':[firstgrade[i]['Grade'], secondgrade[i]['Grade'], thirdgrade[i]['Grade']]}
                grade.append(data)
            return JsonResponse(head)
        else:
            return JsonResponse({'message': 'wrong entry for student id'})
    else:
        return JsonResponse({'message': 'wrong entry for level'})

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
