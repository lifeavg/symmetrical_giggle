from django.urls import include, path

from .rest.routers import router

urlpatterns = [
    path("", include(router.urls)),
]
