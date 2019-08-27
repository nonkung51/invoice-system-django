from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ("name", "tel", "tax_id", "address", "id_number")

