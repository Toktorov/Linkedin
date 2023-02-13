from rest_framework.routers import DefaultRouter

from apps.organizations.views import OrganizationAPIViewSet, PostAPIViewSet, CommentAPIViewSet, LikeAPIViewSet


router = DefaultRouter()
router.register(prefix='organization', viewset=OrganizationAPIViewSet)
router.register(prefix='organization_post', viewset=PostAPIViewSet)
router.register(prefix='organization_comment', viewset=CommentAPIViewSet)
router.register(prefix='organization_like', viewset=LikeAPIViewSet)

urlpatterns = router.urls