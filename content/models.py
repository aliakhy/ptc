from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import *
from .tasks import translatetask


# blog
class Blog(models.Model):
    title = models.CharField(max_length=70, verbose_name="عنوان")
    slug = models.SlugField(max_length=70, unique=True, verbose_name="مسیر")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    summary = models.CharField(max_length=100, blank=True, verbose_name="خلاصه")
    body = RichTextUploadingField(blank=True, verbose_name="متن")
    is_show = models.BooleanField(default=False, verbose_name="نشان داده شود؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین آپدیت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class Comment(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="مقاله")
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="والد"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="published", verbose_name="وضعیت"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("fa", "Farsi"),
        ("ar", "Arabic"),
    ]
    text_fa = models.CharField(max_length=200, blank=True, verbose_name="متن فارسی")
    text_en = models.CharField(max_length=200, blank=True, verbose_name="متن انگلیسی")
    text_ar = models.CharField(max_length=200, blank=True, verbose_name="متن عربی")

    language = models.CharField(
        max_length=10, choices=LANGUAGE_CHOICES, verbose_name="زبان"
    )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        translatetask.delay(self.pk)

    def __str__(self):
        return f"id={self.pk}"

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


# projects
class Project(models.Model):
    title = models.CharField(max_length=70, verbose_name="عنوان")
    slug = models.SlugField(max_length=70, unique=True, verbose_name="شناسه یکتا")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="دسته‌بندی",
    )
    dimensions = models.CharField(max_length=30, blank=True, verbose_name="ابعاد")
    creation_year = models.CharField(
        max_length=4, validators=[is_digit], blank=True, verbose_name="سال ساخت"
    )
    scale = models.PositiveIntegerField(default=1, verbose_name="مقیاس")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"


class Category(models.Model):
    title = models.CharField(max_length=70, verbose_name="عنوان")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class Gallery(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="gallery", verbose_name="پروژه"
    )
    image = models.ImageField(upload_to="project_gallery", verbose_name="تصویر")

    def __str__(self):
        return f"Gallery for {self.project.title}"

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری‌ها"


class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=200, verbose_name="نشانی ایمیل")
    phone_number = models.CharField(
        max_length=11, validators=[is_digit], verbose_name="شماره تماس"
    )
    description = models.TextField(verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس‌ها"


class Order(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="نام شرکت")
    activity_area = models.CharField(max_length=100, verbose_name="حوزه فعالیت")
    email = models.EmailField(max_length=200, verbose_name="نشانی ایمیل")
    contact_number = models.CharField(
        max_length=11, validators=[is_digit], verbose_name="شماره تماس"
    )
    explanation = models.TextField(verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"


class Apply(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("reviewed", "Reviewed"),
    ]

    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=200, verbose_name="نشانی ایمیل")
    phone_number = models.CharField(
        max_length=11, validators=[is_digit], verbose_name="شماره تماس"
    )
    education_degree = models.CharField(max_length=100, verbose_name="مدرک تحصیلی")
    study_field = models.CharField(max_length=100, verbose_name="رشته تحصیلی")
    education_level = models.CharField(max_length=100, verbose_name="مقطع تحصیلی")
    resume = models.FileField(
        validators=[apply_resume_validate], upload_to="resumes", verbose_name="رزومه"
    )
    cover_letter = models.CharField(max_length=100, verbose_name="نامه پوششی")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending", verbose_name="وضعیت"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "درخواست همکاری"
        verbose_name_plural = "درخواست‌های همکاری"


class History(models.Model):
    achievement=models.CharField(max_length=100,blank=True,verbose_name="دستاورد")
    year=models.CharField(max_length=4,verbose_name="سال",validators=[is_digit])
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name = "تاریخچه و دستاورد"
        verbose_name_plural = "تاریخجه و دستاورد ها"