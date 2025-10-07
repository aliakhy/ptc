import pytest
from content.models import History
import json
def create_history():
    hsitory = History.objects.create(
        achievement_en="test",
        achievement_fa="تست",
        achievement_ar="امتحان",
        year='1400'
    )
    return hsitory


@pytest.mark.django_db
@pytest.mark.parametrize(
    "lang_title", [("en", "test"), ("ar", "امتحان"), ("fa", "تست")]
)
def test_get_list_blog(client, lang_title) -> None:
    create_history()
    lang, achievement = lang_title
    if lang == "en":
        url = "/history/"
    else:
        url = f"/{lang}/history/"
    response = client.get(url)
    response_content = json.loads(response.content)["results"][0]
    assert response_content["achievement"] == achievement
    assert response.status_code == 200
