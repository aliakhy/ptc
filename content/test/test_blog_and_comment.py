import pytest
from content.models import Blog, Comment
import json


def create_blog():
    blog = Blog.objects.create(
        title_en="test",
        title_fa="تست",
        title_ar="امتحان",
        summary_en="english",
        summary_fa="فارسی",
        summary_ar="عربی",
        slug="test",
        is_show=True,
    )
    return blog


@pytest.mark.django_db
@pytest.mark.parametrize(
    "lang_title", [("en", "test"), ("ar", "امتحان"), ("fa", "تست")]
)
def test_get_list_blog(client, lang_title) -> None:
    create_blog()
    lang, title = lang_title
    if lang == "en":
        url = "/blog/"
    else:
        url = f"/{lang}/blog/"
    response = client.get(url)
    response_content = json.loads(response.content)["results"][0]
    assert response_content["title"] == title
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize(
    "lang_summary", [("en", "english"), ("ar", "عربی"), ("fa", "فارسی")]
)
def test_get_blog(client, lang_summary) -> None:
    create_blog()
    lang, summary = lang_summary
    if lang == "en":
        url = "/blog/test/"
    else:
        url = f"/{lang}/blog/test/"
    response = client.get(url)
    response_content = json.loads(response.content)
    assert response_content["summary"] == summary
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_comment_list(client) -> None:
    blog = create_blog()
    Comment.objects.create(text_en="test", language="en", blog=blog)
    response = client.get("/blog/test/comments/")
    response_content = json.loads(response.content)["results"][0]
    assert response_content["text_translate"] == "test"
    assert response.status_code == 200
