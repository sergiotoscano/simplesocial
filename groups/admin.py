from django.contrib import admin
from . import models


#this makes possible manage groups memberships within /admin
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
