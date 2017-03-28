"""View definitions for comments."""
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from .filters import CommentFilter
from .serializers import CommentSerializer


class CommentsList(APIView):
    """List all comments, or create new comment."""

    def get(self, request, format=None):
        """List all comments."""
        comm_filters = CommentFilter(request.query_params)

        if comm_filters.is_valid():
            comm_serializer = CommentSerializer(instance=comm_filters.objects(), many=True)

            return Response(data=comm_serializer.data, status=status.HTTP_200_OK)

        return Response(data=comm_filters.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """Create a comment."""
        comm_serializer = CommentSerializer(data=request.data)

        if comm_serializer.is_valid():
            comm_serializer.save()

            return Response(data=comm_serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=comm_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsDetail(APIView):
    """List comment, update comment, or delete comment."""

    def get(self, request, pk, format=None):
        """List comment with id pk if it exists."""
        comment = get_object_or_404(Comment, pk=pk)
        comm_serializer = CommentSerializer(instance=comment)

        return Response(data=comm_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update comment with id pk if it exists."""
        comment = get_object_or_404(Comment, pk=pk)
        comm_serializer = CommentSerializer(instance=comment, data=request.data, partial=True)

        if comm_serializer.is_valid():
            comm_serializer.save()

            return Response(data=comm_serializer.data, status=status.HTTP_200_OK)

        return Response(data=comm_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete comment with id pk if it exists."""
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
