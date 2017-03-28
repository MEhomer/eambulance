"""Serializer classes for the models from models.py"""
from rest_framework import serializers

from .models import Diagnosis


class DiagnosisSerializer(serializers.Serializer):
    """Diagnosis serializer."""

    id = serializers.IntegerField(read_only=True)
    created_timestamp = serializers.DateTimeField(read_only=True)
    from_timestamp = serializers.IntegerField()
    to_timestamp = serializers.IntegerField()
    diagnosis = serializers.CharField(style={'base_template': 'textarea.html'})
    patient = serializers.IntegerField()
    doctor = serializers.IntegerField()

    def create(self, validated_data):
        """Create new diagnosis."""
        return Diagnosis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Updated diagnosis."""
        instance.from_timestamp = validated_data.get('from_timestamp', instance.from_timestamp)
        instance.to_timestamp = validated_data.get('to_timestamp', instance.to_timestamp)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.patient = validated_data.get('patient', instance.patient)
        instance.doctor = validated_data.get('doctor', instance.doctor)
        instance.save()

        return instance
