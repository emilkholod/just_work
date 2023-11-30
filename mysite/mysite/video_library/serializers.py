from django.db.models import F as Field

from rest_framework import serializers

from . import models


class PageListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Page
        fields = ['url', 'title']


class PageInstanceSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = models.Page
        fields = ['url', 'title', 'content']

    @staticmethod
    def get_content_ordering_method(key):
        """
        Return function to content sorting
        """
        return tuple(key[field] for field in models.AbstractContentInfo.Meta.ordering)

    def get_content(self, obj):
        """
        Return list of different contents on the page
        """
        contents: list = []
        for content_serializer in (VideoSerializer, AudioSerializer, TextSerializer):
            content_query = content_serializer.Meta.model.objects.filter(page=obj)
            content_query.update(counter=Field('counter') + 1)
            contents.extend(content_serializer(content_query, many=True).data)

        contents = sorted(contents, key=self.get_content_ordering_method)
        for content in contents:
            content.pop('id')
        return contents


CONTENT_INFO_FIELDS = ['id', 'counter', 'title', 'sequence']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = CONTENT_INFO_FIELDS + ['video_url', 'subtitles_url']


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Audio
        fields = CONTENT_INFO_FIELDS + ['bitrate']


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Text
        fields = CONTENT_INFO_FIELDS + ['text']
