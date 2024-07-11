# authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    full_name = models.CharField(max_length=200)
    admission_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_set',  # Update related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_set',  # Update related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    REQUIRED_FIELDS = ['email', 'full_name', 'admission_number', 'course', 'year_of_study']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
