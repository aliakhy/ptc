from django.db import models
from .validators import *


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11, validators=[is_digit])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    company_name = models.CharField(max_length=100)
    activity_area = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=11,validators=[is_digit])
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Apply(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('reviewed', 'Reviewed'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11, validators=[is_digit])
    education_degree = models.CharField(max_length=100)
    study_field = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    resume = models.FileField(validators=[apply_resume_validate])
    cover_letter = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)