from .serializers import StoveSerializer, BurnerStateSerializer, TemperatureSerializer
from .serializers import BurnerSerializer, RequestBurnerSerializer, PanStateSerializer, PanSerializer
from .serializers import ProgrammingSerializer, ShortcutSerializer
from .models import Stove, BurnerState, Temperature, Burner, RequestBurner, PanState, Pan
from .models import Programming, Shortcut
from rest_framework import viewsets
from rest_framework.response import Response

class StoveViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		queryset = Stove.objects.all()
		stove_token = self.request.query_params.get('token', None)

		if stove_token is not None:
			queryset = queryset.filter(token=stove_token)

		return queryset

	serializer_class = StoveSerializer

class BurnerStateViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		queryset = BurnerState.objects.all()
		burner_state_id = self.request.query_params.get('id', None)
		burner_state_description = self.request.query_params.get('description', None)

		if burner_state_id is not None:
			queryset = queryset.filter(id=burner_state_id)

		if burner_state_description is not None:
			queryset = queryset.filter(description=burner_state_description)

		return queryset

	serializer_class = BurnerStateSerializer

class TemperatureViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		queryset = Temperature.objects.all()

		temperature_id = self.request.query_params.get('id', None)
		temperature_description = self.request.query_params.get('description', None)

		if temperature_id is not None:
			queryset = queryset.filter(id=temperature_id)
		elif temperature_description is not None:
			queryset = queryset.filter(description=temperature_description)

		return queryset

	serializer_class = TemperatureSerializer

class BurnerViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		queryset = Burner.objects.all()

		burner_id = self.request.query_params.get('id', None)
		burner_description = self.request.query_params.get('description', None)

		if burner_id is not None:
			queryset = queryset.filter(id=burner_id)
		elif burner_description is not None:
			queryset = queryset.filter(description=burner_description)

		return queryset

	serializer_class = BurnerSerializer

class RequestBurnerViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		queryset = RequestBurner.objects.all()
		request_burner_id = self.request.query_params.get('id', None)

		if request_burner_id is not None:
			queryset = queryset.filter(id=request_burner_id)

		return queryset

	serializer_class = RequestBurnerSerializer

class PanStateViewSet(viewsets.ModelViewSet):
	queryset = PanState.objects.all()
	serializer_class = PanStateSerializer

class PanViewSet(viewsets.ModelViewSet):
	queryset = Pan.objects.all()
	serializer_class = PanSerializer

class ProgrammingViewSet(viewsets.ModelViewSet):
	queryset = Programming.objects.all()
	serializer_class = ProgrammingSerializer

class ShortcutViewSet(viewsets.ModelViewSet):
	queryset = Shortcut.objects.all()
	serializer_class = ShortcutSerializer
