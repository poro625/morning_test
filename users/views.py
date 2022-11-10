from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.serializers import UserSerializer
# Create your views here.

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"}, status=status.HTTP_201_CREATED)
        return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)