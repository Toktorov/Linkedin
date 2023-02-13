from django.contrib import admin

from apps.organizations.models import Organization, OrganizationPost, OrganizationPostComment, OrganizationPostLike, TrackOrganization

# Register your models here.
admin.site.register(Organization)
admin.site.register(OrganizationPost)
admin.site.register(OrganizationPostComment)
admin.site.register(OrganizationPostLike)
admin.site.register(TrackOrganization)