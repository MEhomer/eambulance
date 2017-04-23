"""Serializer classes for the models from models.py."""
from rest_framework import serializers

from .models import Diagnosis


class DiagnosisSerializer(serializers.Serializer):
    """Diagnosis serializer."""

    id = serializers.IntegerField(read_only=True)
    created_timestamp = serializers.DateTimeField(required=False)
    diagnosis = serializers.CharField(style={'base_template': 'textarea.html'})
    doctor = serializers.IntegerField()
    diagnosis_id = serializers.CharField(style={'base_template': 'textarea.html'})

    # Deprecated
    patient = serializers.IntegerField(required=False)
    from_timestamp = serializers.IntegerField(required=False)
    to_timestamp = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """Create new diagnosis."""
        return Diagnosis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Updated diagnosis."""
        instance.created_timestamp = validated_data.get('created_timestamp', instance.created_timestamp)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.doctor = validated_data.get('doctor', instance.doctor)
        instance.diagnosis_id = validated_data.get('diagnosis_id', instance.diagnosis_id)

        # Deprecated
        instance.patient = validated_data.get('patient', instance.patient)
        instance.from_timestamp = validated_data.get('from_timestamp', instance.from_timestamp)
        instance.to_timestamp = validated_data.get('to_timestamp', instance.to_timestamp)
        instance.save()

        return instance
