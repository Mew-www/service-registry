from django.db import models
import uuid
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Service(models.Model):
    """A connectable service on the internet, be it Load Balancer or datacenter server"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    endpoint_url = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    description_url = models.CharField(max_length=255, blank=True, null=True)
