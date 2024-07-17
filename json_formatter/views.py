from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import JsonRequestSerializer, JsonResponseSerializer
import json


class JsonFormatViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        return Response({"message": "GET request received"})

    @staticmethod
    def create(request):
        serializer = JsonRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data.get('data', {})
            json_str = json.dumps(data, indent=4)
            formatted_string = json_str.replace('\n', '\r\n').replace('"', '\"')
            response_serializer = JsonResponseSerializer(data={'formatted_data': formatted_string})
            if response_serializer.is_valid():
                return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
