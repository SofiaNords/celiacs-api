from rest_framework import generics, permissions
from celiacs_api.permissions import IsOwnerOrReadOnly
from selected.models import Select
from selected.serializers import SelectSerializer


# API view to list and create Select objects
class SelectList(generics.ListCreateAPIView):
    # Allow authenticated users to create, others can only read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Specify the serializer class to use
    serializer_class = SelectSerializer
    # Define the queryset to retrieve all Select objects
    queryset = Select.objects.all()

    # Override the perform_create method to associate
    # the created object with the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# API view to retrieve and destroy Select objects
class SelectDetail(generics.RetrieveDestroyAPIView):
    # Allow only the owner to delete, others can only read
    permission_classes = [IsOwnerOrReadOnly]
    # Specify the serializer class to use
    serializer_class = SelectSerializer
    # Define the queryset to retrieve all Select objects
    queryset = Select.objects.all()
