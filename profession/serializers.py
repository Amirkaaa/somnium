from rest_framework.serializers import ModelSerializer

from .models import Profession


class ProfessionSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

