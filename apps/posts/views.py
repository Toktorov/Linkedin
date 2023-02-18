from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins, permissions

from apps.posts import models, serializer
from apps.posts.permissions import PostPermissions

# Create your views here.
class PostAPIViewSet(GenericViewSet, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin):
    queryset = models.Post.objects.all()
    serializer_class = serializer.PostSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return serializer.PostDetailSerializer
        return serializer.PostSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (permissions.IsAuthenticated(), PostPermissions())
        return (permissions.AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class LikeAPIViewSet(GenericViewSet, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin, 
                    mixins.DestroyModelMixin):
    queryset = models.PostLike.objects.all()
    serializer_class = serializer.PostLikeSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class CommentAPIViewSet(GenericViewSet, 
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = models.PostComment.objects.all()
    serializer_class = serializer.PostCommentSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class PostImagesAPIViewSet(GenericViewSet, 
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = models.PostImages.objects.all()
    serializer_class = serializer.PostImagesSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        post = models.Post.objects.get(id = serializer.initial_data.get("post"))
        if serializer.is_valid() and post.user == request.user:
            serializer.save()
            return Response({"OK" : "Успешно создано"})
        return Response({"Error" : "Вы не можете добавить фотографию"})

class PostFavotiteAPIView(GenericViewSet, 
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = models.PostFavorites.objects.all()
    serializer_class = serializer.PostFavoritesSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)