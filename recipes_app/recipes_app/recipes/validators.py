from re import compile
from django.core.exceptions import ValidationError

pattern = compile(r"^((\w+)(,\s\w+))+$")


def validate_ingredients(input_string):
    if pattern.match(input_string) is None:
        raise ValidationError('The ingredients should be separated by ", "!')