# authentication/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

class CustomUserAdmin(UserAdmin):
    model = Student
    list_display = ['username', 'email', 'full_name', 'admission_number', 'course', 'year_of_study', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Student Details', {'fields': ('full_name', 'admission_number', 'course', 'year_of_study')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name', 'admission_number', 'course', 'year_of_study')}),
    )

admin.site.register(Student, CustomUserAdmin)
