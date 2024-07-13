from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import JsonRequestSerializer, JsonResponseSerializer
import json


class JsonFormatView(APIView):
    def post(self, request):
        serializer = JsonRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            json_str = json.dumps(data, indent=4)
            formatted_string = json_str.replace('\n', '\r\n').replace('"', '\"')
            formatted_string = '{' + formatted_string[1:-1] + '}'
            response_serializer = JsonResponseSerializer(data={'formatted_data': formatted_string})
            if response_serializer.is_valid():
                return Response(response_serializer.data)
        return Response(serializer.errors, status=400)
