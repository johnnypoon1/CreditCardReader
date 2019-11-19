from rest_framework import serializers
from .models import CreditCard

class CCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('ccnumber')