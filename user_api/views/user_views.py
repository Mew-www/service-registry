from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from django.conf import settings

from ..permissions import IsThisUserOrAdministrator
from ..serializers.user import UserSerializer, UserModel


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(operation_id="\U0001F6AB (Administrative)"),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(operation_id="\U0001F6AB (Administrative)"),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(operation_id="\U0001F6AB (Administrative)"),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_summary="\U0001F389 Send a POST request here to create a new account. No authentication required. \U0001F513",
    ),
)
@method_decorator(
    name="update", decorator=swagger_auto_schema(operation_id="users_full_update")
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="\U0001F4CB Send a PATCH request here to update your account data. Get your ID from /me endpoint.",
    ),
)
class UserViewSet(viewsets.ModelViewSet):

    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Set resource permissions explicitly per each action
        """

        # Allow new user creation for anyone, unless settings.ADMIN_ONLY_USERAPI is set True
        if self.action == "create":
            permission_classes = [
                permissions.AllowAny
                if not settings.ADMIN_ONLY_USERAPI
                else permissions.IsAdminUser
            ]

        # Allow Read/Update only for user themselves, or admin
        elif (
            self.action == "retrieve"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            permission_classes = [IsThisUserOrAdministrator]

        # Allow remaining actions (List/Destroy) only for administrators
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]
