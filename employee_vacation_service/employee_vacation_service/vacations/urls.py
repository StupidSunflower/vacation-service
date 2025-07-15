from django.urls import path
from .views import (
    EmployeeListCreateView,
    VacationCreateView,
    EmployeeVacationListView,
    VacationDeleteView
)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('vacations/', VacationCreateView.as_view(), name='vacation-create'),
    path('vacations/employee/<int:employee_id>/', EmployeeVacationListView.as_view(), name='employee-vacations'),
    path('vacations/<uuid:id>/', VacationDeleteView.as_view(), name='vacation-delete'),
]