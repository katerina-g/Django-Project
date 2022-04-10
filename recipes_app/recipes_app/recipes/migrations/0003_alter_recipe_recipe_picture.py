# Generated by Django 3.2.12 on 2022-04-09 06:16

from django.db import migrations, models
import recipes_app.recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220407_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_picture',
            field=models.ImageField(upload_to='mediafiles', validators=[recipes_app.recipes.validators.validate_picture_max_size], verbose_name='Recipe Picture'),
        ),
    ]