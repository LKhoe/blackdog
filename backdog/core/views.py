from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Project, ProjectTeam, TeamPurpose, Organization, TeamMember, OrganizationalRole, TeamMembership
from django.urls import reverse_lazy

from django.contrib import messages
from django.shortcuts import render

from .nossos_scripts import hide_fields

# Telas de funcionamento geral
class HomePageView(TemplateView):
    template_name = "core/home.html"

# class Register(TemplateView):
#     template_name = "bootstrap/register.html"

# class NotFound(TemplateView):
#     template_name = "bootstrap/404.html"

# class Login(TemplateView):
#     template_name = "bootstrap/login.html"

# Telas dos membros de time
class TeamMemberCreate(CreateView):
    model = TeamMember
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('home_page')

class TeamMemberList(ListView):
    model = TeamMember
    template_name = "core/teammember_list.html"

    def get_queryset(self):
        return {'rows' : TeamMember.objects.filter(),
                'cols' : ['Nome', 'CPF', 'Ações']}

class TeamMemberUpdate(UpdateView):
    model = TeamMember
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('team_member_list')

class TeamMemberDelete(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('team_member_list')


# Telas das funções organizacionais
class OrganizationalRoleCreate(CreateView):
    model = OrganizationalRole
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('home_page')

class OrganizationalRoleList(ListView):
    model = OrganizationalRole
    template_name = "core/organizationalrole_list.html"

    def get_queryset(self):
        return {'rows' : OrganizationalRole.objects.filter(),
                'cols' : ['Nome da organização', 'Ações']}

class OrganizationalRoleUpdate(UpdateView):
    model = OrganizationalRole
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('organizational_role_list')

class OrganizationalRoleDelete(DeleteView):
    model = OrganizationalRole
    success_url = reverse_lazy('organizational_role_list')


# Telas dos times de projeto
class ProjectTeamCreate(CreateView):
    model = ProjectTeam
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('home_page')

class ProjectTeamList(ListView):
    model = ProjectTeam
    template_name = "core/projectteam_list.html"

    def get_queryset(self):
        return {'rows' : ProjectTeam.objects.filter(),
                'cols' : ['Nome', 'Ações']}

class ProjectTeamUpdate(UpdateView):
    model = ProjectTeam
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('project_team_list')

class ProjectTeamDelete(DeleteView):
    model = ProjectTeam
    success_url = reverse_lazy('project_team_list')


# Telas do TeamMembership (?) 
# TODO decidir se realmente terão telas pra ele
class TeamMembershipCreate(CreateView):
    model = TeamMembership
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('home_page')

class TeamMembershipUpdate(UpdateView):
    model = TeamMembership
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('team_membership_list')

class TeamMembershipList(ListView):
    model = TeamMembership
    template_name = "core/teammembership_list.html"

    def get_queryset(self):
        return {'rows' : TeamMembership.objects.filter(),
                'cols' : ['Time', 'Membro', 'Função Organizacional', 'Ações']}

class TeamMembershipDelete(DeleteView):
    model = TeamMembership
    success_url = reverse_lazy('team_membership_list')


# Telas dos propositos do time
class TeamPurposeCreate(CreateView):
    model = TeamPurpose
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('home_page')

class TeamPurposeUpdate(UpdateView):
    model = TeamPurpose
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('team_purpose_list')

class TeamPurposeList(ListView):
    model = TeamPurpose
    template_name = 'core/teampurpose_list.html'

    def get_queryset(self):
        return {'rows' : TeamPurpose.objects.filter(),
                'cols' : ['Propósito', 'Time', 'Ações']}

class TeamPurposeDelete(DeleteView):
    model = TeamPurpose
    success_url = reverse_lazy('team_purpose_list')


# Telas dos projetos
class ProjectCreate(CreateView):
    model = Project
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('project_list')

class ProjectUpdate(UpdateView):
    model = Project
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('project_list')

class ProjectList(ListView):
    model = Project
    template_name = "core/project_list.html"

    def get_queryset(self):
        return {'rows' : Project.objects.filter(),
                'cols' : ['Nome do projeto', 'Descrição', 'Organização', 'Ações']}

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

# Telas das organizações
class OrganizationCreate(CreateView):
    model = Organization
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('home_page')

class OrganizationList(ListView):
    model = Organization
    template_name = "core/organization_list.html"

    def get_queryset(self):
        return {'rows' : Organization.objects.filter(),
                'cols' : ['Nome da organização', 'CNPJ', 'Ações']}

class OrganizationUpdate(UpdateView):
    model = Organization
    fields = hide_fields(model, ['habilitado'])
    success_url = reverse_lazy('organization_list')

class OrganizationDelete(DeleteView):
    model = Organization
    success_url = reverse_lazy('organization_list')
