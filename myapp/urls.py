from .views import student_list , student_detail , student_create , student_update , student_delete , register_user
from django.urls import path

urlpatterns = [
    path('students/', student_list.as_view()),
    path('students/<int:pk>/', student_detail),
    path('students/create/', student_create),
    path('students/update/<int:pk>/', student_update),
    path('students/delete/<int:pk>/', student_delete),
    path('register/', register_user),
]