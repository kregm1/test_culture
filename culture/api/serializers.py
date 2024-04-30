from rest_framework import serializers
from api.models import Theatre


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'
