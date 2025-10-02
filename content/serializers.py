from rest_framework import serializers

from .models import *


#   -------->projects
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["image"]


class ProjectDetailSerializer(serializers.ModelSerializer):
    gallery_item = GallerySerializer(many=True, source="gallery")

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "creation_year",
            "scale",
            "dimensions",
            "gallery_item",
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField(source="get_first_image")

    class Meta:
        model = Project
        fields = ["id", "title", "category", "creation_year", "first_image"]

    def get_first_image(self, obj):
        first = obj.gallery.first()
        if first:
            return f"http://127.0.0.1:8000{first.image.url}"
        return None


#   _________>blog


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "description", "summary", "body"]


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "description", "summary"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "parent", "updated_at"]

    def validate_parent(self, value):
        if value and value.status != "Published":
            raise serializers.ValidationError("Parent comment must be Published.")
        return value


#     -------->aplly
class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "education_degree",
            "study_field",
            "education_level",
            "resume",
            "cover_letter",
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "phone_number", "description"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "company_name",
            "activity_area",
            "email",
            "contact_number",
            "explanation",
        ]
