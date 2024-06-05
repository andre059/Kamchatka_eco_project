from rest_framework import serializers

from trails.models import Trail


class TrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'
