from django.contrib import admin
from . import models
# Register your models here.


class GroupMemberInLine(admin.TabularInLine):
# this is for the inline admin interface.
    model = models.GroupMember
# it allows us to utilize the admin interface in django website
# provides ability to edit models on the same page as the parent model.



admin.site.register(models.Group)
