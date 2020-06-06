from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
import uuid

from ..models.service import Service
from ..serializers.service import ServiceSerializer
from ..permissions import IsOwner


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return (
            Service.objects.filter(user=self.request.user)
            if self.request.user.is_authenticated
            else Service.objects.none()
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["get"], detail=False, url_path=r"by_name/(?P<name>[^/]+)")
    def get_service_by_name(self, request, name):
        try:
            id_as_name = uuid.UUID(name)
        except ValueError:
            id_as_name = None

        if id_as_name:
            s = Service.objects.filter(user=request.user, id__exact=id_as_name).first()
        else:
            s = Service.objects.filter(user=request.user, name__exact=name).first()

        if s:
            return Response(data=ServiceSerializer(s).data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
