from rest_framework import status as http_status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import Response

from api import serializers
from api.services import nlp_model


def base_view(request, handler_func):
    serializer = serializers.InputTextSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)
    validated_data = serializer.validated_data
    text = validated_data['text']
    response = handler_func(text)
    return Response(data=response, status=http_status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def tokenize_view(request):
    handler_func = nlp_model.tokenize_text
    return base_view(request, handler_func)


@api_view(['POST'])
@permission_classes([AllowAny])
def pos_tag_view(request):
    handler_func = nlp_model.pos_tagging
    return base_view(request, handler_func)


@api_view(['POST'])
@permission_classes([AllowAny])
def ner_view(request):
    handler_func = nlp_model.entity_recognition
    return base_view(request, handler_func)
