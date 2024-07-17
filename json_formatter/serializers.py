from rest_framework import serializers


class JsonRequestSerializer(serializers.Serializer):
    data = serializers.JSONField(required=False)


class JsonResponseSerializer(serializers.Serializer):
    formatted_data = serializers.CharField()
