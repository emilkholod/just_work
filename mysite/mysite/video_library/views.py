from rest_framework import viewsets
from rest_framework.response import Response

from .models import Page
from .serializers import PageInstanceSerializer, PageListSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Return instance specific data
        """
        instance = self.get_object()
        serializer = PageInstanceSerializer(instance, context={'request': request})
        return Response(serializer.data)
