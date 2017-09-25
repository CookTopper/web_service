from models import Stove
from rest_framework import serializers

class StoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stove
        fields = [
            'id',
            'token',
        ]