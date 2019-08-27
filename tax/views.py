from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Bill, Field
import json


class BillView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        if request.method == "POST":
            json_data = json.loads(request.body)
            bill = Bill(people_id=json_data["people_id"], name=json_data["name"])
            bill.save()
            for field in json_data["fields"]:
                Field(
                    field_name=field["name"], field_value=field["value"], bill=bill
                ).save()

        return Response(json_data)

