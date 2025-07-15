from rest_framework import serializers
from .models import Employee, Vacation

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class VacationSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacation
        fields = ['id', 'employee', 'employee_id', 'start_date', 'end_date', 'created', 'modified']
        read_only_fields = ['id', 'created', 'modified', 'employee']

    def validate_employee_id(self, value):
        if not Employee.objects.filter(id=value).exists():
            raise serializers.ValidationError("Employee with this ID does not exist")
        return value

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        employee = Employee.objects.get(id=employee_id)
        return Vacation.objects.create(employee=employee, **validated_data)