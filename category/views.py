from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serializers import CategorySerializer
from celiacs_api.permissions import IsOwnerOrReadOnly


# View for listing and creating categories
class CategoryList(generics.ListCreateAPIView):
    # Specify the serializer class to use
    serializer_class = CategorySerializer

    # Set the permission classes for the view
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Define the queryset
    queryset = Category.objects.all()

    # Specify the filter backends to use for filtering, searching, and ordering
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    # Define the fields that can be used for filtering
    filterset_fields = [
        'name',
    ]


# View for retrieving, updating and deleting a specific category
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # Specify the serialixer class to use
    serializer_class = CategorySerializer

    # Set the permission classes for the view
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Define the queryset
    queryset = Category.objects.all()
