from django.views.generic import TemplateView

from .models import Employee


class EmployeeHierarchyView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context
