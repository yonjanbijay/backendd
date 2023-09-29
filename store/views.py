from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MSerializer
from .serializers import PSerializer
from .models import motorcycle
from .models import motorcycleParts


class MView(viewsets.ModelViewSet):
    serializer_class = MSerializer
    queryset = motorcycle.objects.all()

class PView(viewsets.ModelViewSet):
    serializer_class = PSerializer
    queryset = motorcycleParts.objects.all()
