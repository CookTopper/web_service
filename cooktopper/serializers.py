from models import Stove, BurnerState, Temperature, Burner, PanState, Pan, ProgrammingType, ProgrammingDetails, Programming, Shortcut
from rest_framework import serializers

class StoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stove
        fields = [
            'id',
            'token'
        ]

class BurnerStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BurnerState
        fields = [
            'id',
            'description'
        ]

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = [
            'id',
            'description'
        ]

class BurnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burner
        fields = [
            'id',
            'description',
            'stove',
            'temperature',
            'burner_state'
        ]

class PanStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanState
        fields = [
            'id',
            'description'
        ]

class PanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pan
        fields = [
            'id',
            'code',
            'temperature',
            'pan_state'
        ]

class ProgrammingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingType
        fields = [
            'id',
            'description'
        ]

class ProgrammingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingDetails
        fields = [
            'id',
            'programmed_hour',
            'expected_duration',
            'programming_type',
            'temperature'
        ]

class ProgrammingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programming
        fields = [
            'id',
            'burner',
            'programming_details'
        ]

class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = [
            'id',
            'description',
            'programming_details'
        ]