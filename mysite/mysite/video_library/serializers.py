from rest_framework import serializers

from .models import Page


class PageListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['url', 'title']


class PageInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['url', 'title']
