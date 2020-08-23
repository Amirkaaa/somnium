from rest_framework.serializers import ModelSerializer

from group.models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
