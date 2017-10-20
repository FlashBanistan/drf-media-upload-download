from rest_framework import viewsets
from upload.serializers import UploadSerializer
from upload.models import Upload

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer