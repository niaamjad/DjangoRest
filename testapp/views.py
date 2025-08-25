from django.shortcuts import render
import requests
import json


def StudentList(request):
    response = requests.get('http://127.0.0.1:8000/myapp/students').json()
    return render(request, 'student_list.html', {'students': response})
    

def StudentCreate(request):
    instance = {'Name': 'Ali', 'FamilyName': 'Ahmadi', 'Code': 5}
    jsondata = json.dumps(instance)
    header = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:8000/myapp/students/create/', data=jsondata, headers=header)
    return response
