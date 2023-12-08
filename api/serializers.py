from rest_framework.serializers import ModelSerializer
from .models import Sanction


class SanctionSerializer(ModelSerializer):
    class Meta:
        model = Sanction
        fields = '__all__'