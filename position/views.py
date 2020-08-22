from rest_framework.viewsets import ModelViewSet

from .serializers import PositionSerializer
from .models import Position


# Create your views here.
class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
