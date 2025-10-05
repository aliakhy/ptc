import pytest
from content.models import Project, Gallery
import json
from django.core.files.uploadedfile import SimpleUploadedFile


def create_project():
    project = Project.objects.create(
        title_en="test",
        title_fa="تست",
        title_ar="امتحان",
        description_en="english",
        description_fa="فارسی",
        description_ar="عربی",
        slug="test",
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    "lang_title", [("en", "test"), ("ar", "امتحان"), ("fa", "تست")]
)
def test_get_list_blog(client, lang_title) -> None:
    create_project()
    lang, title = lang_title
    if lang == "en":
        url = "/projects/"
    else:
        url = f"/{lang}/projects/"
    response = client.get(url)
    response_content = json.loads(response.content)["results"][0]
    assert response_content["title"] == title
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize(
    "lang_summary", [("en", "english"), ("ar", "عربی"), ("fa", "فارسی")]
)
def test_get_blog(client, lang_summary) -> None:
    create_project()
    lang, description = lang_summary
    if lang == "en":
        url = "/projects/test/"
    else:
        url = f"/{lang}/projects/test/"
    response = client.get(url)
    response_content = json.loads(response.content)
    assert response_content["description"] == description
    assert response.status_code == 200
