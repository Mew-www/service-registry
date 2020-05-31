from django.contrib import admin
from django.urls import path, include
from config.doc_generator import schema_view, token_schema_decor
from user_api.views.user_views import UserViewSet
from user_api.views.user_token_refresh import refresh_auth_token
from user_api.views.me_endpoint import MeApiView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("users", UserViewSet, basename="User")

urlpatterns = [
    path("admin/", admin.site.urls),  # in-built adminsite
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="api-doc",),
    path(
        "v1/",
        include(
            [
                # Paths are resolved in-order, place any non-router paths here above
                path("api-token-auth/", token_schema_decor(obtain_auth_token)),
                path("api-token-refresh/", token_schema_decor(refresh_auth_token)),
                path("users/me/", MeApiView.as_view()),
                path("", include(router.urls)),
            ]
        ),
    ),
]
