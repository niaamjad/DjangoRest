from rest_framework import serializers
from .models import Student , Scores
from django.contrib.auth.models import User


class studentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ScoreSrializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source = "student.Name") 
    class Meta:
        model = Scores
        fields = ['student_name','score']
