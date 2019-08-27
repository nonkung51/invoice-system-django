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
        if self.request.GET.get("delete_id"):
            try:
                People.objects.filter(
                    id_number=self.request.GET.get("delete_id")
                ).delete()
            except:
                pass
        people = People.objects.all()
        output = []
        for indv in people:
            output.append(
                {
                    "id": indv.id_number,
                    "name": indv.name,
                    "address": indv.address,
                    "tel": indv.tel,
                }
            )
        return Response(output)

    def post(self, request, format=None):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
