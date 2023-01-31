from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.posts.models import Post
from apps.posts.serializer import PostSerializer, PostDetailSerializer, PostLikeSerializer, PostCommentSerializer, PostFavoritesSerializer, PostImagesSerializer
from apps.posts.permissions import PostPermissions
from apps.posts.models import Post, PostImages, PostLike, PostComment, PostFavorites

# Create your views here.
class PostAPIViewSet(GenericViewSet, ListModelMixin,
                        CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return PostDetailSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), PostPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class LikeAPIViewSet(GenericViewSet, ListModelMixin,
                        CreateModelMixin, DestroyModelMixin):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class CommentAPIViewSet(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class PostImagesAPIViewSet(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        post = Post.objects.get(id = serializer.initial_data.get("post"))
        if serializer.is_valid() and post.user == request.user:
            serializer.save()
            return Response({"OK" : "Успешно создано"})
        return Response({"Error" : "Вы не можете добавить фотографию"})

class PostFavotiteAPIView(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = PostFavorites.objects.all()
    serializer_class = PostFavoritesSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)