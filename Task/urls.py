from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Task Management API",
      default_version='v1',
      description="API documentation for the Task Management App",
      contact=openapi.Contact(email="your-email@example.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)
from drf_yasg.app_settings import swagger_settings

# Set global token auth scheme for Swagger UI
#To chnage ur username and password to TOKEN AUTHENTICATION FORM
swagger_settings.SECURITY_DEFINITIONS = {
    'Token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Paste your token like this: Token <your_token>',
    }
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
