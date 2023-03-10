# Generated by Django 4.1.7 on 2023-03-08 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_privileges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=200)),
                ('u_password', models.CharField(max_length=200)),
                ('u_email', models.CharField(max_length=200)),
                ('u_tel', models.IntegerField()),
                ('u_create_at', models.DateTimeField(auto_now_add=True)),
                ('u_update_at', models.DateTimeField(auto_now=True)),
                ('u_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_users', to='Main.department')),
                ('u_faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_users', to='Main.faculty')),
                ('u_privilege', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privilege_users', to='Main.user_privileges')),
            ],
        ),
    ]
