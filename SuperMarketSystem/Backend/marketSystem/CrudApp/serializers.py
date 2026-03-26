from rest_framework import serializers
from . models import SuperMarketSystem

class SuperMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMarketSystem
        fields = '__all__'