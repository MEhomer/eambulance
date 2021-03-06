"""Serializer classes for the mozels from models.py."""
from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.Serializer):
    """Comment serializer."""

    id = serializers.IntegerField(read_only=True)
    created_timestamp = serializers.DateTimeField(required=False)
    patient = serializers.IntegerField()
    from_timestamp = serializers.IntegerField()
    to_timestamp = serializers.IntegerField()
    comment = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """Create new comment."""
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update instance."""
        instance.created_timestamp = validated_data.get('created_timestamp', instance.created_timestamp)
        instance.patient = validated_data.get('patient', instance.patient)
        instance.from_timestamp = validated_data.get('from_timestamp', instance.from_timestamp)
        instance.to_timestamp = validated_data.get('to_timestamp', instance.to_timestamp)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()

        return instance
