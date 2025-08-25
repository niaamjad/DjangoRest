from django.urls import path
from .views import StudentList , StudentCreate

urlpatterns = [
    path('students/', StudentList),
    path('students/create/', StudentCreate),
]