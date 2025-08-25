from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User


class studentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']