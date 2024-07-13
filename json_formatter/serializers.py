from rest_framework import serializers


class JsonRequestSerializer(serializers.Serializer):
    data = serializers.JSONField()


class JsonResponseSerializer(serializers.Serializer):
    formatted_data = serializers.CharField()
