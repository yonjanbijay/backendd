from rest_framework import serializers
from .models import motorcycle
from .models import motorcycleParts


class MSerializer(serializers.ModelSerializer):
    class Meta:
        model = motorcycle
        fields = ('id', 'motorcycle_model', 'description',
                  'image', 'price',)


class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = motorcycleParts
        fields = ('partName', 'description',
                  'image', 'price', )
