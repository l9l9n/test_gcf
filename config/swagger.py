from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="l9l9ndos@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)
