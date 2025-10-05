import pytest
from content.models import Order, Apply, Contact
import json
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_create_order(client) -> None:
    response = client.post(
        "/how-to-create/",
        data={
            "company_name": "a",
            "activity_area": "area",
            "email": "a@gmail.com",
            "contact_number": "9112656",
            "explanation": "explane",
        },
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content["company_name"] == "a"
    assert response_content["contact_number"] == "9112656"


@pytest.mark.django_db
def test_create_contact(client) -> None:
    response = client.post(
        "/contact-us/",
        data={
            "first_name": "a",
            "last_name": "a",
            "email": "a@gmail.com",
            "phone_number": "9112656",
            "description": "explane",
        },
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content["first_name"] == "a"
    assert response_content["last_name"] == "a"
    assert response_content["phone_number"] == "9112656"


@pytest.mark.django_db
def test_create_aplly(client) -> None:
    pdf_file = SimpleUploadedFile(
        name="test_file.pdf",
        content=b"%PDF-1.4 test pdf content",
        content_type="application/pdf",
    )

    response = client.post(
        "/membership/",
        data={
            "first_name": "a",
            "last_name": "a",
            "email": "a@gmail.com",
            "phone_number": "9112656",
            "education_degree": "a",
            "study_field": "a",
            "education_level": "a",
            "resume": pdf_file,
            "cover_letter": "aaaaa",
        },
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content["first_name"] == "a"
    assert response_content["last_name"] == "a"
    assert response_content["education_degree"] == "a"
    assert response_content["education_level"] == "a"
    assert response_content["cover_letter"] == "aaaaa"
