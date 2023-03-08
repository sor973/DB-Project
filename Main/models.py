from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)

class User_privileges(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    u_id = models.IntegerField(default=0,unique=True)
    u_name = models.CharField(max_length=200)
    u_password = models.CharField(max_length=200)
    u_email = models.CharField(max_length=200)
    u_tel = models.IntegerField()
    u_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty_users')
    u_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_users')
    u_privilege = models.ForeignKey(User_privileges, on_delete=models.CASCADE, related_name='privilege_users')
    u_create_at = models.DateTimeField(auto_now_add=True)
    u_update_at = models.DateTimeField(auto_now=True)
