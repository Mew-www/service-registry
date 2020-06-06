from django.db import models
import uuid
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Service(models.Model):
    """A connectable service on the internet, be it Load Balancer or datacenter server"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    endpoint_url = models.CharField(
        # unique so that no two service entries forward to same address
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    name = models.CharField(
        # unique so that name lookup is guaranteed to work
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    description_url = models.CharField(max_length=255, blank=True, null=True)
