from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import *


# blog
class Blog(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField()
    summary = models.CharField(max_length=100)
    body = RichTextUploadingField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    text = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id={self.pk}"


# projects
class Project(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    dimensions = models.CharField(max_length=30)
    creation_year = models.CharField(max_length=4, validators=[is_digit])
    scale = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="gallery"
    )
    image = models.ImageField(upload_to="project_gallery")

    def __str__(self):
        return f"Gallery for {self.project.title}"


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
    contact_number = models.CharField(max_length=11, validators=[is_digit])
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Apply(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("reviewed", "Reviewed"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11, validators=[is_digit])
    education_degree = models.CharField(max_length=100)
    study_field = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    resume = models.FileField(validators=[apply_resume_validate], upload_to="resumes")
    cover_letter = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
