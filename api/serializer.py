from rest_framework import serializers
from .models import Student, FirstQuarter, SecondQuarter, ThirdQuarter, FourthQuarter

class FirstQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstQuarter
        fields =['Subject', 'Grade']

class SecondQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondQuarter
        fields =['Subject', 'Grade']

class ThirdQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdQuarter
        fields =['Subject', 'Grade']

class FourthQuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourthQuarter
        fields =['Subject', 'Grade']

class StudentSerializer(serializers.ModelSerializer):
    firstgrade = FirstQuarterSerializer(many=True, read_only=True)
    secondgrade = SecondQuarterSerializer(many=True, read_only=True)
    thirdgrade = ThirdQuarterSerializer(many=True, read_only=True)
    fourthgrade = FourthQuarterSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields =["Name", "LRN", "Status", "Section", "Quarter", "firstgrade","secondgrade","thirdgrade","fourthgrade"]
        depth = 1