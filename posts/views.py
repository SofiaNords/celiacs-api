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

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            # Översätt användarvänliga termer till interna koder
            score_translation = {
                'Okay': 'OK',
                'Good': 'GD',
                'Great': 'GT',
            }
            translated_query = score_translation.get(search_query, search_query)
            queryset = queryset.filter(score=translated_query)
        return queryset

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
