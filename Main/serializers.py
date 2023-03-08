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
    u_faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    u_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    u_privilege = serializers.PrimaryKeyRelatedField(queryset=User_privileges.objects.all())

    class Meta:
        model = User
        fields = ['id', 'u_name', 'u_password', 'u_email', 'u_tel', 'u_faculty', 'u_department', 'u_privilege', 'u_create_at', 'u_update_at']
