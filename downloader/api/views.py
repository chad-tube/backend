from django.core.cache import cache

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from downloader.services.youtube import fetch_download_details


"""
{
    "url": "https://www.youtube.com/watch?v=Bs9-j-8swxQ"
}

{
"url": "https://www.youtube.com/watch?v=WwEcPcfRlD0",
"type_": "video"
}
"""


class TYPE_CHOICES:
    ALL = "all"
    VIDEO = "video"
    AUDIO = "audio"


class ListTypeChoices(APIView):
    def get(self, request):
        return Response(
            {
                "choices": [
                    {"value": TYPE_CHOICES.ALL, "label": "All"},
                    {"value": TYPE_CHOICES.VIDEO, "label": "Video"},
                    {"value": TYPE_CHOICES.AUDIO, "label": "Audio"},
                ]
            }
        )


class DownloadView(APIView):
    class InputSerializer(serializers.Serializer):
        TYPE_CHOICES_ = (
            (TYPE_CHOICES.VIDEO, "Video"),
            (TYPE_CHOICES.AUDIO, "Audio"),
            (TYPE_CHOICES.ALL, "All"),
        )

        url = serializers.URLField(required=True)
        type_ = serializers.ChoiceField(choices=TYPE_CHOICES_, default=TYPE_CHOICES.ALL)

    class OutputSerializer(serializers.Serializer):
        title = serializers.CharField(required=True)
        thumbnail_url = serializers.URLField(required=True)
        streams = serializers.ListField(required=True)

    def get(self, request):
        return Response({"message": "Hello, world!"})

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {}
        if cache.get(serializer.validated_data["url"]):
            data = cache.get(serializer.validated_data["url"])
            return Response(data)
        else:
            data = fetch_download_details(
                serializer.validated_data["url"], serializer.validated_data["type_"]
            )
            cache.set(serializer.validated_data["url"], data, timeout=60 * 60 * 24)

        output_serializer = self.OutputSerializer(data=data)
        output_serializer.is_valid(raise_exception=True)
        return Response(output_serializer.data)
