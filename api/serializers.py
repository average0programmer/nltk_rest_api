from rest_framework import serializers


class InputTextSerializer(serializers.Serializer):
    text = serializers.CharField(allow_null=False, allow_blank=True, required=True)
