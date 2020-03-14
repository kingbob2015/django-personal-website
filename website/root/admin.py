from django.contrib import admin

from .models import Person, Skill, Link


class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'tag_line', 'email', 'picture', 'description']


class SkillAdmin(admin.ModelAdmin):
    fields = ['person', 'skill']


class LinkAdmin(admin.ModelAdmin):
    fields = ['person', 'link_name', 'link_url']


admin.site.register(Person, PersonAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Link, LinkAdmin)
