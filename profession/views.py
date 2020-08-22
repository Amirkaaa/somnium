from rest_framework.viewsets import ModelViewSet

from .serializers import ProfessionSerializer
from .models import Profession


# Create your views here.
class ProfessionViewSet(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
