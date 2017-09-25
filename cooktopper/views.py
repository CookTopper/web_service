from rest_framework import viewsets
from .serializers import StoveSerializer
from .models import Stove

class StoveViewSet(viewsets.ModelViewSet):
	queryset = Stove.objects.all()
	serializer_class = StoveSerializer