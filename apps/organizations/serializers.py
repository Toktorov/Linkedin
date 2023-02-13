from rest_framework import serializers

from apps.organizations.models import Organization, OrganizationPost, OrganizationPostComment, OrganizationPostLike


class OrganizationPostLike(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPostLike
        fields = ('id', 'user', 'post')

class OrganizationPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPostComment
        fields = ('id', 'post', 'user', 'comment', 'created')

class OrganizationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPost
        fields = ('id', 'organization', 'title', 'image', 'created')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'title', 'description', 'logo', 'banner', 'created')