from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from celiacs_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    # Serializer class to use for listing and creating comments
    serializer_class = CommentSerializer

    # Permission classes to apply; allows authenticated users to create
    # others can only read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Queryset to use for retrieving comments
    queryset = Comment.objects.all()

    # Backend to use for filtering the queryset
    filter_backends = [DjangoFilterBackend]

    # Fields to filter the queryset by
    filterset_fields = ['post']

    def perform_create(self, serializer):
        # Save the new comment with the owner set to the current user
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # Permission class to apply; only the owner can update or delete
    permission_classes = [IsOwnerOrReadOnly]

    # Serializer class to use for retrieving, updating, and deleting comments
    serializer_class = CommentDetailSerializer

    # Queryset to use for retrieving comments
    queryset = Comment.objects.all()
