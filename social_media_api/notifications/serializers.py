from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source="actor.username")
    target_type = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ["id", "actor", "verb", "target_type", "created_at", "read"]

    def get_target_type(self, obj):
        return obj.content_type.model if obj.content_type else None