from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        try:
            return UserProfile.objects.get(user=self.request.user)
        except Exception as e:
            raise Http404

    def get(self, request, format=None):
        user_profile = self.get_object()
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

