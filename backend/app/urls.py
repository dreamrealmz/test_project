from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Shop",
        default_version='v1',
        description="swagger для тестового задания",
        terms_of_service="https://disk.yandex.ru/i/kAJJlny9Z9T5YQ",
        contact=openapi.Contact(email="ad.azarov17@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('shops.urls')),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
