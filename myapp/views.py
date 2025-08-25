from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Scores, Student 
from .serializer import ScoreSrializer, studentSerialize , UserSerialize 
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView
from .permission import IsSuperUserOrReadOnly
from .pagination import StudentPagination


class student_list(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerialize
    permission_classes = ((IsSuperUserOrReadOnly,))
    pagination_class = StudentPagination



@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = studentSerialize(student, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def student_create(request):
    serializer = studentSerialize(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    serializer = studentSerialize(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response("Item successfully deleted!")



@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerialize(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['message'] = "Successfully registered a new user."
            data['token'] = Token.objects.get(user=user).key
        return Response(data)



@api_view(['GET'])
def StudentScores(requests):
    score = Scores.objects.all()
    score_serilizer = ScoreSrializer(score,many = True)
    return Response(score_serilizer.data)


