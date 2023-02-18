from rest_framework import serializers

from apps.posts import models


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostImages
        fields = ('post', 'image')

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLike
        fields = ('user', 'post')

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostComment
        fields = ('user', 'post')

class PostFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostFavorites
        fields = ('user', 'post')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = "__all__"

class PostDetailSerializer(serializers.ModelSerializer):
    #post - посты
    post_likes = PostLikeSerializer(read_only = True, many = True)
    count_likes = serializers.SerializerMethodField(read_only = True)
    #comments - комментарии
    post_comments = PostCommentSerializer(read_only = True, many = True)
    count_comments = serializers.SerializerMethodField(read_only = True)
    #post favorites - избранные
    post_favotites = PostFavoritesSerializer(read_only = True, many = True)
    count_post_favotites = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = models.Post
        fields = ('id', 'title',
            'created', 'user', 'count_likes', 
            'post_likes', 'post_comments', 'count_comments',
            'post_favotites', 'count_post_favotites'
        )

    def get_count_likes(self, instance):
        return instance.post_likes.all().count()

    def get_count_comments(self, instance):
        return instance.post_comments.all().count()

    def get_count_post_favotites(self, instance):
        return instance.post_favotites.all().count()