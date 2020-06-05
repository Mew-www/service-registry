from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.user import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        responses={
            "200": openapi.Response("User object including the {ID}", UserSerializer),
        }
    ),
)
class MeApiView(APIView):
    """Returns the user's own data (including ID, necessary for sending PATCH request to update fields)."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Serialize request.user, request context is required for HyperlinkedIdentityField
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)
