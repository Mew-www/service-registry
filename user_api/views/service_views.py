from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.service import Service
from ..serializers.service import ServiceSerializer
from ..permissions import IsThisUserOrAdministrator, IsOwner


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Service.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
