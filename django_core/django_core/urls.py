"""django_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unittest.mock import patch
import os
from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .settings import HOST_URL
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


def patch_the_method(func):
    def inner(*args, **kwargs):
        with patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True):
            response = func(*args, **kwargs)
        return response

    return inner


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    url=HOST_URL,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
                  re_path('admin/', admin.site.urls),
                  re_path(r'^auth/', include('djoser.urls')),
                  re_path(r'^auth/', include('djoser.urls.authtoken')),
                  path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
                  path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
                  # re_path(r'^auth/', include("djoser.urls.jwt")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
