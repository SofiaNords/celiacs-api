from rest_framework import serializers
from posts.models import Post
from selected.models import Select


# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    # Read-only field to display the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')

    # Field to determine if the current user is the owner of the post
    is_owner = serializers.SerializerMethodField()

    # Read-only field to display the profile ID of the owner
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    # Read-only field to display the profile image URL of the owner
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # Field to get the ID of the select object related to the post
    select_id = serializers.SerializerMethodField()

    # Read-only field to display the count of comments on the post
    comments_count = serializers.ReadOnlyField()

    # Read-only field to display the count of selects on the post
    select_count = serializers.ReadOnlyField()

    # Method to validate the image field
    def validate_image(self, value):
        # Check if the image size is larger than 2MB
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        # Check if the image width is larger than 4096px
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        # Check if the image height is larger than 4096px
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    # Method to determine if the current user is the owner of the post
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Method to get the ID of the select object related to the post
    def get_select_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            select = Select.objects.filter(
                owner=user, post=obj
            ).first()
            return select.id if select else None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'location', 'content', 'image',
            'select_id', 'comments_count', 'select_count',
        ]
