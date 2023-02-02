from django.contrib import admin

from apps.posts.models import Post, PostImages, PostLike, PostComment, PostFavorites

# Register your models here.
admin.site.register(Post)
admin.site.register(PostImages)
admin.site.register(PostLike)
admin.site.register(PostComment)
admin.site.register(PostFavorites)