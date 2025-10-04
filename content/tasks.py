from celery import shared_task
from deep_translator import GoogleTranslator
@shared_task
def translatetask(comment_id):
    from .models import Comment

    comment = Comment.objects.get(pk=comment_id)

    if comment.language == "en" and comment.text_en:
        comment.text_fa = GoogleTranslator(source="en", target="fa").translate(
            comment.text_en
        )
        comment.text_ar = GoogleTranslator(source="en", target="ar").translate(
            comment.text_en
        )
    elif comment.language == "fa" and comment.text_fa:
        comment.text_en = GoogleTranslator(source="fa", target="en").translate(
            comment.text_fa
        )
        comment.text_ar = GoogleTranslator(source="fa", target="ar").translate(
            comment.text_fa
        )
    elif comment.language == "ar" and comment.text_ar:
        comment.text_en = GoogleTranslator(source="ar", target="en").translate(
            comment.text_ar
        )
        comment.text_fa = GoogleTranslator(source="ar", target="fa").translate(
            comment.text_ar
        )
    comment.save()