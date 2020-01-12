from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from .models import Letter, Description
from ..files.models import File
from ..files.serializers import FileSerializer
from .serializers import LetterSerializer, DescriptionSerializer
from django.utils.decorators import method_decorator


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


@method_decorator(name="list", decorator=swagger_auto_schema(tags=["letters", "files"]))
@method_decorator(
    name="create", decorator=swagger_auto_schema(tags=["letters", "files"])
)
@method_decorator(
    name="partial_update", decorator=swagger_auto_schema(tags=["letters", "files"])
)
@method_decorator(
    name="update", decorator=swagger_auto_schema(tags=["letters", "files"])
)
@method_decorator(
    name="destroy", decorator=swagger_auto_schema(tags=["letters", "files"])
)
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(letter=self.kwargs["letter_pk"]).all()
