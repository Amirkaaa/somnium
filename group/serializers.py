from rest_framework.serializers import ModelSerializer, SerializerMethodField

from group.models import Group
from position.serializers import PositionTreeSerializer


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupTreeSerializer(ModelSerializer):
    branches = SerializerMethodField()
    positions = SerializerMethodField()

    def get_branches(self, obj):
        branches_serializer = GroupTreeSerializer(data=obj.branches.all(), many=True)
        branches_serializer.is_valid()

        return branches_serializer.data

    def get_positions(self, obj):
        position_serializer = PositionTreeSerializer(data=obj.positions.all(), many=True)
        position_serializer.is_valid()

        return position_serializer.data

    class Meta:
        model = Group
        fields = '__all__'
