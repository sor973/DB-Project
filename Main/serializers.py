from rest_framework import serializers
from Main.models import Faculty, Department, User_privileges, User

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class User_privilegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_privileges
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    u_faculty = FacultySerializer()
    u_department = DepartmentSerializer()
    u_privilege = User_privilegesSerializer()

    class Meta:
        model = User
        fields = ['id', 'u_id', 'u_name', 'u_email', 'u_tel', 'u_faculty', 'u_department', 'u_privilege', 'u_create_at', 'u_update_at']
