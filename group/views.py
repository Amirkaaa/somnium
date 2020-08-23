from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from group.serializers import GroupSerializer
from group.tree_serializer import GroupTreeSerializer
from group.models import Group


# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(detail=False, methods=['GET'])
    def tree(self, request):
        parents = Group.objects.filter(director=None)

        parents_serializer = GroupTreeSerializer(data=parents, many=True)
        parents_serializer.is_valid()

        return Response(data=parents_serializer.data, status=status.HTTP_200_OK)
