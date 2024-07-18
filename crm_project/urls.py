# crm_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("autopulse_app.urls")),
    path("api/", include("autopulse_app.api_urls")),  # Include API routes
]
