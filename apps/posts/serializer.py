from rest_framework import serializers

from apps.posts.models import Post, PostImages, PostLike, PostComment, PostFavorites


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ('post', 'image')

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('user', 'post')

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ('user', 'post')

class PostFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFavorites
        fields = ('user', 'post')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
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
        model = Post
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