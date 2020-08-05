from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=200)
    cnpj = models.BigIntegerField(unique=True)

    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200,unique=True)

    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProjectTeam(Team):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True)


class TeamPurpose(models.Model):
    description = models.TextField()
    project_team = models.ForeignKey(ProjectTeam, on_delete=models.CASCADE)

    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.project_team+": "+self.description


class Person(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.BigIntegerField(unique=True)

    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TeamMember(Person):
    pass


class OrganizationalRole(models.Model):
    name = models.CharField(max_length=200)

    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    organizational_role = models.ForeignKey(OrganizationalRole, on_delete=models.CASCADE)
    
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.member.name+" no time "+self.team.name+" sendo "+self.organizational_role.name
