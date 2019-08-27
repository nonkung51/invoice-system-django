from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import PeopleSerializer
from .models import People

# Create your views here.
class PeopleView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        people = People.objects.all()
        output = []
        for indv in people:
            output.append({
                "id": indv.id_number,
                "name": indv.name,
                "address": indv.address,
                "tel": indv.tel
            })
        return Response(output)
