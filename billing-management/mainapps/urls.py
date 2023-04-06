from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/v1/", include("usom.urls", namespace="usom_api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
