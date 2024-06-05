from rest_framework import serializers

from trails.models import Trail, Rule, Notification


class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
