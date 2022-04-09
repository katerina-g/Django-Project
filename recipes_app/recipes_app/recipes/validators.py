from re import compile
from django.core.exceptions import ValidationError

pattern = compile(r"^(([a-zA-Z0-9\s](,)?)*)+$")


def validate_ingredients(input_string):
    if pattern.match(input_string) is None:
        raise ValidationError('The ingredients should be separated by ", "!')


def validate_picture_max_size(width=640, height=520):
    def validator_image(image):
        error = False
        if width is not None and image.width > width:
            error = True
        if height is not None and image.height > height:
            error = True
        if error:
            raise ValidationError(
                f'Size should be max 640 x 520 pixels.'
            )

    return validator_image
