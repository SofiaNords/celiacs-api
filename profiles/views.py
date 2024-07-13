from django.db.models import Count
from rest_framework import generics, filters
from celiacs_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# View for listing profiles
class ProfileList(generics.ListAPIView):
    # Define the queryset with annotated fields for posts and selects count
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        selected_count=Count('owner__select', distinct=True)
    ).order_by('-created_at')
    # Specify the serializer class to use
    serializer_class = ProfileSerializer
    # Specify the filter backends to use for ordering
    filter_backends = [
        filters.OrderingFilter
    ]
    # Define the fields that can be used for ordering
    ordering_fields = [
        'posts_count',
        'selected_count',
    ]


# View for retrieving and updating a specific profile
class ProfileDetail(generics.RetrieveUpdateAPIView):
    # Set the permission classes for the view
    permission_classes = [IsOwnerOrReadOnly]
    # Define the queryset with annotated fields for posts and selects count
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        selected_count=Count('owner__select', distinct=True)
    ).order_by('-created_at')
    # Specify the serializer class to use
    serializer_class = ProfileSerializer
    # Specify the filter backends to use for ordering
    filter_backends = [
        filters.OrderingFilter
    ]
    # Define the fields that can be used for ordering
    ordering_fields = [
        'posts_count',
        'selected_count',
    ]
    # Specify the serializer class to use (repeated for clarity)
    serializer_class = ProfileSerializer
