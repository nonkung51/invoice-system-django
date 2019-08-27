from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from tax.models import Field, Bill
from people.models import People
import json


class PrintView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        bill_list = Bill.objects.filter(proving_state=4)

        out = []

        for bill in bill_list:
            try:
                p = People.objects.get(id_number=str(bill.people_id))
                field_list = []
                fields = Field.objects.filter(bill=bill)
                for field in fields:
                    field_list.append(
                        {"name": field.field_name, "value": field.field_value}
                    )
                out.append(
                    {
                        "id": bill.id,
                        "name": bill.name,
                        "people": {
                            "name": p.name,
                            "address": p.address,
                            "tel": p.tel,
                            "taxId": p.tax_id,
                            "idNumber": p.id_number,
                        },
                        "fields": field_list,
                    }
                )
            except Exception as e:
                print(e)

        return Response(out)
    
    def delete(self, request, format=None):
    # {"id": approve_id_of_bill}
        if request.method == "DELETE":
            json_data = json.loads(request.body)
            bill_id = json_data["id"]
            Bill.objects.filter(
                    id=bill_id
                ).delete()

        return Response({})
