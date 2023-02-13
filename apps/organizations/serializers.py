from rest_framework import serializers

from apps.organizations.models import Organization, OrganizationPost, OrganizationPostComment, OrganizationPostLike, TrackOrganization


class TrackOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackOrganization
        fields = ('id', 'user', 'organization')

class OrganizationPostLikeSerializer(serializers.ModelSerializer):
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

class OrganizationDetailSerializer(serializers.ModelSerializer):
    #track - отслеживание организации
    tracks_organization = TrackOrganizationSerializer(read_only = True, many = True)
    count_tracks = serializers.SerializerMethodField(read_only = True)
    #posts - посты организации
    organizations_posts = OrganizationPostSerializer(read_only = True, many = True)
    count_posts = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Organization
        fields = ('id', 'title', 'description', 'logo', 
                  'banner', 'created', 'tracks_organization', 
                  'count_tracks', 'organizations_posts', 'count_posts')

    def get_count_tracks(self, instance):
        return instance.tracks_organization.all().count()

    def get_count_posts(self, instance):
        return instance.organizations_posts.all().count()

    def get_count_comments(self, instance):
        return instance.organization_post_comments.all().count()