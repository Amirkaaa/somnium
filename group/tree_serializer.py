from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth import get_user_model

from position.models import Position
from group.models import Group


class UserTreeSerializer(ModelSerializer):
    subordination = SerializerMethodField()

    @staticmethod
    def get_subordination(obj):
        subordination_serializer = GroupTreeSerializer(data=obj.subordination.all(), many=True)
        subordination_serializer.is_valid()

        return subordination_serializer.data

    class Meta:
        model = get_user_model()
        fields = '__all__'


class PositionTreeSerializer(ModelSerializer):
    user = UserTreeSerializer()

    class Meta:
        model = Position
        exclude = ['group']


class GroupTreeSerializer(ModelSerializer):
    branches = SerializerMethodField()
    positions = SerializerMethodField()

    @staticmethod
    def get_branches(obj):
        branches_serializer = GroupTreeSerializer(data=obj.branches.all(), many=True)
        branches_serializer.is_valid()

        return branches_serializer.data

    @staticmethod
    def get_positions(obj):
        position_serializer = PositionTreeSerializer(data=obj.positions.all(), many=True)
        position_serializer.is_valid()

        return position_serializer.data

    class Meta:
        model = Group
        fields = '__all__'