from rest_framework import serializers
from .models import Profile


# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    # Read-only field to display the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')

    # Field to determine if the current user is the owner of the profile
    is_owner = serializers.SerializerMethodField()

    # Read-only field to display the count of posts by the owner
    posts_count = serializers.ReadOnlyField()

    # Read-only field to display the count of selected items by the owner
    selected_count = serializers.ReadOnlyField()

    # Method to determine if the current user is the owner of the profile
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Meta class to define serializer options
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'posts_count',
            'selected_count',
        ]
