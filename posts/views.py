from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from celiacs_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


# View for listing and creating posts
class PostList(generics.ListCreateAPIView):
    # Specify the serializer class to use
    serializer_class = PostSerializer

    # Set the permission classes for the view
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Define the queryset with annotated fields for comments and selects count
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        select_count=Count('select', distinct=True)
    ).order_by('-created_at')
    # Specify the filter backends to use for filtering, searching, and ordering
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    # Define the fields that can be used for filtering
    filterset_fields = [
        'select__owner__profile',
        'owner__profile',
    ]
    # Define the fields that can be used for searching
    search_fields = [
        'owner__username',
        'title',
        'location',
    ]
    # Define the fields that can be used for ordering
    ordering_fields = [
        'comments_count',
        'selected_count',
        'selected__created_at'
    ]

    # Method to save the owner of the post when creating a new post
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# View for retrieving, updating, and deleting a specific post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # Specify the serializer class to use
    serializer_class = PostSerializer

    # Set the permission classes for the view
    permission_classes = [IsOwnerOrReadOnly]

    # Define the queryset with annotated fields for comments and selects count
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        select_count=Count('select', distinct=True)
    ).order_by('-created_at')
    # Specify the filter backends to use for ordering
    filter_backends = [
        filters.OrderingFilter,
    ]
    # Define the fields that can be used for ordering
    ordering_fields = [
        'comments_count',
        'selected_count',
        'selected__created_at'
    ]
