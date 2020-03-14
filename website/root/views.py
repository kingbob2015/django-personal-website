from django.views import generic

from .models import Person


class IndexView(generic.base.TemplateView):
    template_name = "root/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['person'] = Person.objects.get()
        except Person.DoesNotExist:
            context['error_no_person'] = "No person was in the database"

        return context
