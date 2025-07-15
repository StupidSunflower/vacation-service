from rest_framework import generics
from .models import Employee, Vacation
from .serializers import EmployeeSerializer, VacationSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class VacationCreateView(generics.ListCreateAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer

    def perform_create(self, serializer):
        employee_id = serializer.validated_data['employee'].id
        if not Employee.objects.filter(id=employee_id).exists():
            raise serializers.ValidationError("Employee does not exist")
        serializer.save()

class EmployeeVacationListView(generics.ListAPIView):
    serializer_class = VacationSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Vacation.objects.filter(employee__employee_id=employee_id).order_by('-start_date')[:3]

class VacationDeleteView(generics.DestroyAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
    lookup_field = 'id'