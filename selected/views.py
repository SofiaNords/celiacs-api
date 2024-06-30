from rest_framework import generics, permissions
from celiacs_api.permissions import IsOwnerOrReadOnly
from selected.models import Select
from selected.serializers import SelectSerializer


class SelectList(generics.ListCreateAPIView):
    """
    List selected or create a select if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SelectSerializer
    queryset = Select.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SelectDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SelectSerializer
    queryset = Select.objects.all()