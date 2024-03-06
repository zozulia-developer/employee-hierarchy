from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import EmployeeForm, PositionForm
from .models import Employee, Position


class EmployeeHierarchyView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employees.html'
    context_object_name = 'employees'
    ordering = ['last_name', 'first_name', 'middle_name']
    paginate_by = 10

    def get_queryset(self):
        sort_by = self.request.GET.get('sort')
        if sort_by:
            return Employee.objects.all().order_by(sort_by)
        return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort', '')
        return context

    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query')
        sort_field = request.POST.get('sort_field')
        employees = Employee.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(middle_name__icontains=search_query) |
            Q(position__name__icontains=search_query) |
            Q(hire_date__icontains=search_query) |
            Q(email__icontains=search_query)
        )
        if sort_field:
            employees = employees.order_by(sort_field)

        paginator = Paginator(employees, self.paginate_by)
        page = request.GET.get('page')
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)

        data = [{'id': employee.id,
                 'first_name': employee.first_name,
                 'last_name': employee.last_name,
                 'middle_name': employee.middle_name,
                 'position': employee.position.name,
                 'hire_date': employee.hire_date,
                 'email': employee.email} for employee in employees]

        return JsonResponse(data, safe=False)


class CreateEmployeeView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/create_employee.html'
    success_url = '/employees/'


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/update_employee.html'
    success_url = '/employees/'


class DeleteEmployeeView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')


class CreatePositionView(CreateView):
    model = Position
    form_class = PositionForm
    template_name = 'employee/create_position.html'
    success_url = reverse_lazy('employee_list')
