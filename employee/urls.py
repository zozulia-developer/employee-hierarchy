from django.urls import path

from .views import (
    CreateEmployeeView, CreatePositionView, DeleteEmployeeView, EmployeeHierarchyView, EmployeeListView,
    EmployeeUpdateView,
)

urlpatterns = [
    path('', EmployeeHierarchyView.as_view(), name='home'),

    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', CreateEmployeeView.as_view(), name='create_employee'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='update_employee'),
    path('employees/<int:pk>/delete/', DeleteEmployeeView.as_view(), name='delete_employee'),

    path('positions/create/', CreatePositionView.as_view(), name='create_position'),
]
