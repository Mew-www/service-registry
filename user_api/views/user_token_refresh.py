from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class AuthTokenRefresh(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # Delete old token (if exists)
        Token.objects.filter(user=user).delete()
        # Create new token in place
        token, _created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


refresh_auth_token = AuthTokenRefresh.as_view()
