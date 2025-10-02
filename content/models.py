from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from submissions.validators import is_digit
#blog
class Blog(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField()
    summary = models.CharField(max_length=100)
    body=RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    text = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id={self.pk}'



#projects
class Project(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    dimensions = models.CharField(max_length=30)
    creation_year = models.CharField(max_length=4,validators=[is_digit])
    is_show = models.BooleanField(default=False)
    scale=models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title



class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_gallery')

    def __str__(self):
        return f"Gallery for {self.project.title}"



