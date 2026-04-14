from rest_framework import viewsets
from rest_framework.permissions import AllowAny

permission_classes = [AllowAny]
from .models import Program, Student
from .serializers import ProgramSerializer, StudentSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()   # ✅ fixed (was Program.objects.all())
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]