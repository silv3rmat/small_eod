from rest_framework_nested import routers
from .views import LetterViewSet, FileViewSet

from django.urls import path, re_path, include

router = routers.SimpleRouter()
router.register("letters", LetterViewSet)

file_router = routers.NestedSimpleRouter(router, "letters", lookup="letter")
file_router.register("files", FileViewSet, basename="letter-files")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(file_router.urls)),
]
