from django.urls import path

from .views import EmployeeHierarchyView

urlpatterns = [
    path('', EmployeeHierarchyView.as_view(), name='home'),
]
