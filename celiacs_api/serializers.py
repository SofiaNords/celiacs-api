from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    # Serializer to include additional fields for the current user.

    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        # Extend the fields from UserDetailsSerializer.
        # Meta to include profile_id and profile_image.
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
            )
