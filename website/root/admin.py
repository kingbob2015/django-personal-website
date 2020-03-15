from django.contrib import admin

from .models import Person, Skill, Link, Project, ProjectTechnology


class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'tag_line', 'email', 'picture', 'description']


class SkillAdmin(admin.ModelAdmin):
    fields = ['person', 'skill']


class LinkAdmin(admin.ModelAdmin):
    fields = ['person', 'link_name', 'link_url']


class ProjectAdmin(admin.ModelAdmin):
    fields = ['person', 'picture', 'name', 'tag_line', 'link_url', "type"]


class ProjectTechnologyAdmin(admin.ModelAdmin):
    fields = ['project', 'technology']


admin.site.register(Person, PersonAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTechnology, ProjectTechnologyAdmin)
