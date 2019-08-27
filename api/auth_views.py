from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import status
from django.http import Http404
from .serializers import UserSerializer


@api_view(["POST"])
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
