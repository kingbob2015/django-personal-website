from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tag_line = models.CharField(max_length=500)
    email = models.EmailField()
    picture = models.CharField(max_length=50)  # Just the name of the file stored in the static files
    description = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.person.name} is skilled in {self.skill}'


class Link(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=50)
    link_url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.link_name} linked to {self.link_url}'


class Project(models.Model):

    project_types = [
        ("Personal", "Personal"),
        ("Professional", "Professional"),
    ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    picture = models.CharField(max_length=50)  # Just the name of the file stored in the static files
    name = models.CharField(max_length=50)
    tag_line = models.CharField(max_length=250)
    link_url = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=25, choices=project_types)

    def __str__(self):
        return f'{self.name}: {self.tag_line}'


class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.technology} used in {self.project.name}'