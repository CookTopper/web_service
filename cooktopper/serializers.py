from cooktopper.models import Stove, BurnerState, Temperature, Burner, RequestBurner, PanState, Pan, Programming, Shortcut
from rest_framework import serializers

class StoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stove
        fields = [
            'id',
            'token',
			'mac_address'
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
            'burner_state',
			'time'
        ]

class RequestBurnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = RequestBurner
		fields = [
			'id',
			'burner_id',
			'new_temperature',
			'new_burner_state',
			'programmed_time',
			'programming_id'
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

class ProgrammingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programming
        fields = [
            'id',
            'temperature',
            'burner_state',
			'programmed_time',
			'expected_duration',
			'creation_time'
        ]

class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = [
            'id',
            'description',
            'programming'
        ]
