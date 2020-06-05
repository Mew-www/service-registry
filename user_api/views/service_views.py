from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.service import Service
from ..serializers.service import ServiceSerializer
from ..permissions import IsThisUserOrAdministrator


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Service.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        # Require login to GET list of objects or POST a new object
        if self.action == "list" or self.action == "create":
            return [IsAuthenticated()]

        # Short-circuit for unauthenticated & require object ownership (or admin for recovery or maintenance, w.e.)
        else:
            return [IsAuthenticated(), IsThisUserOrAdministrator()]
