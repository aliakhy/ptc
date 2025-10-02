from django.core.exceptions import ValidationError
import os
def apply_resume_validate(value):
    name=os.path.splitext(value.name)[1]
    if name.lower() !='.pdf' :
        raise ValidationError('Please upload a pdf file')
    elif  value.size >5*1024*1024:
        raise ValidationError('file is too big')

def is_digit(value):
    if not value.isdigit():
        raise ValidationError('Please enter a number')
