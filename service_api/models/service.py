from django.db import models
import uuid
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Service(models.Model):
    """A connectable service on the internet, be it Load Balancer or datacenter server"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    endpoint_url = models.CharField(
        # required so that service always forwards to an address
        max_length=255,
        blank=False,
        null=False,
    )
    name = models.CharField(
        # required so that name lookup is guaranteed to work
        max_length=255,
        blank=False,
        null=False,
    )
    description_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (
            # ensure that no two services (of a user) would forward to same address
            ("user", "endpoint_url"),
            # ensure that name lookup always matches to same service
            ("user", "name"),
        )
