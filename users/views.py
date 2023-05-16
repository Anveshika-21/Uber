from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import *
from users.serializers import*

class GetStudentsView(APIView):
    def get(self,request):
        print("req",request.GET)
        name=request.GET.get("myname")
        print("name",name)
        if name:
            instance = Students.objects.filter(name=name)
        else:
            instance = Students.objects.all()
        serializers = StudentsSerializers(instance,many=True)
        return Response(data=serializers.data)
    def post(self,request):
        params = request.data
        print("params",params)
        if'address' in params:
            serializer = StudentsSerializers(data=params)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response({"message","Done"})

