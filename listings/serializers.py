from rest_framework import serializers
from .models import Agent, Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()
    class Meta:
        model = Agent
        fields = '__all__'

    def get_properties(self, obj):
        serializer = PropertySerializer(obj.properties.all(), many=True)
        return serializer.data

