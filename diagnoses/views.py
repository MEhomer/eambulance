"""View definitions for diagnosis."""
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Diagnosis
from .filters import DiagnosisFilter
from .serializers import DiagnosisSerializer


class DiagnosesList(APIView):
    """List all diagnoses, or create new diagnosis."""

    def get(self, request, format=None):
        """List all diagnoses."""
        diag_filters = DiagnosisFilter(request.query_params)

        if diag_filters.is_valid():
            diag_serializers = DiagnosisSerializer(instance=diag_filters.objects(), many=True)

            return Response(data=diag_serializers.data, status=status.HTTP_200_OK)

        return Response(data=diag_filters.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """Create new diagnosis."""
        diag_serializer = DiagnosisSerializer(data=request.data)

        if diag_serializer.is_valid():
            diag_serializer.save()

            return Response(data=diag_serializer.data, status=status.HTTP_200_OK)

        return Response(data=diag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiagnosesDetail(APIView):
    """List a diagnosis, update a diagnosis, or delete a diagnosis."""

    def get(self, request, pk, format=None):
        """List a diagnosis if it exists."""
        diagnosis = get_object_or_404(Diagnosis, pk=pk)

        diag_serializer = DiagnosisSerializer(instance=diagnosis)

        return Response(data=diag_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update a diagnosis if it exists."""
        diagnosis = get_object_or_404(Diagnosis, pk=pk)

        diag_serializer = DiagnosisSerializer(instance=diagnosis, data=request.data, partial=True)

        if diag_serializer.is_valid():
            diag_serializer.save()

            return Response(data=diag_serializer.data, status=status.HTTP_200_OK)

        return Response(data=diag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete a diagnosis if it exists."""
        diagnosis = get_object_or_404(Diagnosis, pk=pk)
        diagnosis.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
