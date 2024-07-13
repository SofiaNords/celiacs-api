from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # Read-only field to display the username of the comment owner
    owner = serializers.ReadOnlyField(source='owner.username')

    # Custom method field to check if the current user
    # is the owner of the comment
    is_owner = serializers.SerializerMethodField()

    # Read-only field to display the profile ID of the comment owner
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    # Read-only field to display the profile image URL of the comment owner
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # Custom method field to display the created time
    # in a human-readable format
    created_at = serializers.SerializerMethodField()

    # Custom method field to display the updated time
    # in a human-readable format
    updated_at = serializers.SerializerMethodField

    def get_is_owner(self, obj):
        # Check if the current user is the owner of the comment
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        # Return the created time in a human-readable format
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        # Return the updated time in a human-readable format
        return naturaltime(ojb.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    # Read-only field to display the post ID related to the comment
    post = serializers.ReadOnlyField(source='post.id')
