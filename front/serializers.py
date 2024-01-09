from rest_framework import serializers
from .models import edu

class eduSerializer(serializers.ModelSerializer):
    class Meta:
        model = edu
        fields = '__all__'