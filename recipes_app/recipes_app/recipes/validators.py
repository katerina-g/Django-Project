from re import compile
from django.core.exceptions import ValidationError

pattern = compile(r"^(([a-zA-Z0-9\s](,)?)*)+$")


def validate_ingredients(input_string):
    if pattern.match(input_string) is None:
        raise ValidationError('The ingredients should be separated by ", "!')
