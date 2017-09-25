from rest_framework import viewsets
from .serializers import StoveSerializer, BurnerStateSerializer, TemperatureSerializer
from .serializers import BurnerSerializer, PanStateSerializer, PanSerializer
from .serializers import ProgrammingTypeSerializer, ProgrammingDetailsSerializer
from .serializers import ProgrammingSerializer, ShortcutSerializer
from .models import Stove, BurnerState, Temperature, Burner, PanState, Pan
from .models import ProgrammingType, ProgrammingDetails, Programming, Shortcut

class StoveViewSet(viewsets.ModelViewSet):
	queryset = Stove.objects.all()
	serializer_class = StoveSerializer

class BurnerStateViewSet(viewsets.ModelViewSet):
	queryset = BurnerState.objects.all()
	serializer_class = BurnerStateSerializer

class TemperatureViewSet(viewsets.ModelViewSet):
	queryset = Temperature.objects.all()
	serializer_class = TemperatureSerializer

class BurnerViewSet(viewsets.ModelViewSet):
	queryset = Burner.objects.all()
	serializer_class = BurnerSerializer

class PanStateViewSet(viewsets.ModelViewSet):
	queryset = PanState.objects.all()
	serializer_class = PanStateSerializer

class PanViewSet(viewsets.ModelViewSet):
	queryset = Pan.objects.all()
	serializer_class = PanSerializer

class ProgrammingTypeViewSet(viewsets.ModelViewSet):
	queryset = ProgrammingType.objects.all()
	serializer_class = ProgrammingTypeSerializer

class ProgrammingDetailsViewSet(viewsets.ModelViewSet):
	queryset = ProgrammingDetails.objects.all()
	serializer_class = ProgrammingDetailsSerializer

class ProgrammingViewSet(viewsets.ModelViewSet):
	queryset = Programming.objects.all()
	serializer_class = ProgrammingSerializer

class ShortcutViewSet(viewsets.ModelViewSet):
	queryset = Shortcut.objects.all()
	serializer_class = ShortcutSerializer