from rest_framework import serializers

from trails.models import Trail, Rule, Notification, Park


class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'


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


class ClusterInfoNalichevoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Park
        fields = '__all__'
