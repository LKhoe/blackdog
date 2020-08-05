from django.contrib import admin
from django.urls import path

from .views import (HomePageView, #Register, Login, NotFound,
                    OrganizationCreate, OrganizationDelete, OrganizationList, OrganizationUpdate,
                    ProjectCreate, ProjectList, ProjectUpdate, ProjectDelete,
                    ProjectTeamCreate, ProjectTeamList, ProjectTeamUpdate, ProjectTeamDelete,
                    OrganizationalRoleCreate, OrganizationalRoleDelete, OrganizationalRoleList, OrganizationalRoleUpdate,
                    TeamMemberCreate, TeamMemberList, TeamMemberUpdate, TeamMemberDelete,
                    TeamMembershipCreate, TeamMembershipList, TeamMembershipUpdate, TeamMembershipDelete,
                    TeamPurposeCreate, TeamPurposeList, TeamPurposeUpdate, TeamPurposeDelete)

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    # path('index.html/', HomePageView.as_view(), name='home_page'),
    # path('register.html/', Register.as_view(), name='register'),
    # path('notfound.html/', NotFound.as_view(), name='notfound'),
    # path('login.html', Login.as_view(), name='login'),

    path('organization/', OrganizationList.as_view(), name='organization_list'),
    path('project/', ProjectList.as_view(), name='project_list'),
    path('team_member/', TeamMemberList.as_view(), name='team_member_list'),
    path('project_team/', ProjectTeamList.as_view(), name='project_team_list'),
    path('organizational_role/', OrganizationalRoleList.as_view(), name='organizational_role_list'),
    path('team_purpose/', TeamPurposeList.as_view(), name='team_purpose_list'),
    path('team_membership/', TeamMembershipList.as_view(), name='team_membership_list'),

    path('organization/add/', OrganizationCreate.as_view(), name='organization_add'),
    path('project/add/', ProjectCreate.as_view(), name='project_add'),
    path('team_member/add', TeamMemberCreate.as_view(), name='team_member_add'),
    path('project_team/add/', ProjectTeamCreate.as_view(), name='project_team_add'),
    path('organizational_role/add/', OrganizationalRoleCreate.as_view(), name='organizational_role_add'),
    path('team_purpose/add/', TeamPurposeCreate.as_view(), name='team_purpose_add'),
    path('team_membership/add', TeamMembershipCreate.as_view(), name='team_membership_add'),

    path('organization/<int:pk>/update/', OrganizationUpdate.as_view(), name='organization_update'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project_update'),
    path('team_member/<int:pk>/update/', TeamMemberUpdate.as_view(), name='team_member_update'),
    path('projectteam/<int:pk>/update/', ProjectTeamUpdate.as_view(), name='projectteam_update'),
    path('organizational_role/<int:pk>/update/', OrganizationalRoleUpdate.as_view(), name='organizational_role_update'),
    path('team_purpose/<int:pk>/update/', TeamPurposeUpdate.as_view(), name='team_purpose_update'),
    path('team_membership/<int:pk>/update/', TeamMembershipUpdate.as_view(), name='team_membership_update'),

    path('organization/<int:pk>/delete/', OrganizationDelete.as_view(), name='organization_delete'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project_delete'),
    path('team_member/<int:pk>/delete/', TeamMemberDelete.as_view(), name='team_member_delete'),
    path('projectteam/<int:pk>/delete/', ProjectTeamDelete.as_view(), name='projectteam_delete'),
    path('organizational_role/<int:pk>/delete/', OrganizationalRoleDelete.as_view(), name='organizational_role_delete'),
    path('team_purpose/<int:pk>/delete/', TeamPurposeDelete.as_view(), name='team_purpose_delete'),
    path('team_membership/<int:pk>/delete/', TeamMembershipDelete.as_view(), name='team_membership_delete'),
]
