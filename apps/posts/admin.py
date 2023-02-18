from django.contrib import admin

from apps.posts import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.PostImages)
admin.site.register(models.PostLike)
admin.site.register(models.PostComment)
admin.site.register(models.PostFavorites)