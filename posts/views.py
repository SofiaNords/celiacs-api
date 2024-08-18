from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from celiacs_api.permissions import IsOwnerOrReadOnly
from .models import Post, Category
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
        'score',
    ]
    # Define the fields that can be used for searching
    search_fields = [
        'owner__username',
        'title',
        'location',
        'category__name',
        'score',
    ]
    # Define the fields that can be used for ordering
    ordering_fields = [
        'comments_count',
        'selected_count',
        'selected__created_at',
        'score',
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
        'selected__created_at',
        'score',
    ]

    def get_object(self):
        # This method will be called to retrieve the object
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        
        # Use get_object_or_404 to ensure a 404 response if the object is not found
        obj = get_object_or_404(queryset, **filter_kwargs)
        
        # Check permissions
        self.check_object_permissions(self.request, obj)
        
        return obj
