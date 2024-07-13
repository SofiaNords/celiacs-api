from django.db import IntegrityError
from rest_framework import serializers
from selected.models import Select


# Serializer for the Select model
class SelectSerializer(serializers.ModelSerializer):
    # Read-only field to display the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')

    # Meta class to define serializer options
    class Meta:
        model = Select
        fields = ['id', 'created_at', 'owner', 'post']

    # Method to handle creation of a new Select instance
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            # Raise a validation error if there is an IntegrityError
            # (e.g., duplicate entry)
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
