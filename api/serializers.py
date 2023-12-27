# api/serializers.py

from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField(source="description", required=False)
    snippet = serializers.CharField()
    url = serializers.CharField()
    image_url = serializers.CharField()
    language = serializers.CharField()
    published_at = serializers.DateTimeField()
    source = serializers.CharField()



    # You may want to include other fields based on your requirements

