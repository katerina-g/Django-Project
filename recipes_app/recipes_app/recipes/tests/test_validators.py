import unittest
from django.core.exceptions import ValidationError

from recipes_app.recipes.validators import validate_picture_max_size


class FakeFile:
    width = 641
    height = 521


class ValidatePictureMaxSize(unittest.TestCase):
    def test_when_file_is_bigger__expect_to_raise(self):
        validator = validate_picture_max_size()

        file = FakeFile()

        with self.assertRaises(ValidationError) as context:
            validator(file)
        print(context.exception)
        self.assertIsNotNone(context.exception)



