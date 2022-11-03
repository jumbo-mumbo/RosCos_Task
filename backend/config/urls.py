from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from .routers import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("music.urls"))
    # path("api/", include(router.urls)),
]
