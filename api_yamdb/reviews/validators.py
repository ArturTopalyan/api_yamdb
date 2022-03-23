import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


def year_validator(value):
    if value > datetime.datetime.now().year:
        raise ValidationError(
            '%(value) не может быть больше текущего года!',
            params={'value': value},
        )
