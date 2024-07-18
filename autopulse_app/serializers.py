# serializers.py
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "vin",
            "imei",
            "name",
            "renter_name",
            "monthly_limit",
            "oil_change",
            "financial",
            "status",
            "user",
            "final_odometer",
        ]
        read_only_fields = ["user"]

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["user"] = request.user
        return super().create(validated_data)
