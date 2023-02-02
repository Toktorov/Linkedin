from django.contrib import admin

from apps.users.models import User, UserContact, TypeEmployment, WorkExperience, JobType, Education, Skills

# Register your models here.
admin.site.register(User)
admin.site.register(UserContact)
admin.site.register(TypeEmployment)
admin.site.register(WorkExperience)
admin.site.register(JobType)
admin.site.register(Education)
admin.site.register(Skills)