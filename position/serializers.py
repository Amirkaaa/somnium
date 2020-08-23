from rest_framework.serializers import ModelSerializer

from position.models import Position


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class PositionUserSerializer(ModelSerializer):
    class Meta:
        model = Position
        exclude = ['user']
        depth = 1
