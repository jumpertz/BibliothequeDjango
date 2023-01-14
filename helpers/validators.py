import re
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    pattern = re.compile(r'^(?:\+\d{1,3}[-.\s]?)?\d{10}$')
    if not pattern.match(value):
        raise ValidationError("Le numéro de téléphone n'est pas valide.")
    return value

