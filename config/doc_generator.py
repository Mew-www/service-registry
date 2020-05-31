from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator


class CustomSchemaGenerator(OpenAPISchemaGenerator):
    """
    Re-order specific ViewSets to pre-deterministic order
    """

    def get_paths_object(self, paths):
        return openapi.Paths(
            {
                p: paths[p]
                for x in ["api-token-auth", "api-token-refresh", "users"]
                for p in list(paths.keys())
                if p.startswith(x, 1)
            }
        )


schema_view = get_schema_view(
    openapi.Info(
        title="Service Registry's API",
        default_version="v0.0.0",
        description="RESTful API<br>"
        "/users/ endpoints are administrative<br>"
        "other endpoints are generally used by services (using administratively distributed token)<br>",
        terms_of_service="http://www.latlmes.com/arts/return-of-the-golden-age-of-comics-1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomSchemaGenerator,
)

token_schema_decor = swagger_auto_schema(
    method="POST",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "username": openapi.Schema(type=openapi.TYPE_STRING),
            "password": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={"200": openapi.Response('{"token": "...api-token..."}')},
    operation_summary="Tokens don't expire - regenerating a new token invalidates old token.",
)
