from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(ProjectTeam)
admin.site.register(Person)
admin.site.register(TeamMember)
admin.site.register(OrganizationalRole)
admin.site.register(TeamMembership)
admin.site.register(TeamPurpose)
