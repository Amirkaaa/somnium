from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from position.serializers import PositionUserSerializer


class UserSerializer(ModelSerializer):
    positions = SerializerMethodField()

    @staticmethod
    def get_positions(obj):
        position_serializer = PositionUserSerializer(data=obj.positions.all(), many=True)
        position_serializer.is_valid()

        return position_serializer.data

    class Meta:
        model = get_user_model()
        fields = '__all__'

