from django.db.utils import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        try:
            super().save(**kwargs)
        except IntegrityError as e:
            if "endpoint_url" in str(e):
                raise ValidationError("this endpoint_url already exists")
            elif "name" in str(e):
                raise ValidationError("this service name already exists")
            else:
                raise ValidationError(str(e))

    class Meta:
        model = Service
        fields = "__all__"
        read_only_fields = ["user"]
