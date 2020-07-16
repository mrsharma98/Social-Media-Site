from django.contrib import admin
from . import models
# Register your models here.


class GroupMemberInLine(admin.TabularInLine):
# this is for the inline admin interface.
    model = models.GroupMember



admin.site.register(models.Group)
