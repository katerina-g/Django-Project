# Generated by Django 3.2.12 on 2022-04-07 14:45

from django.db import migrations, models
import recipes_app.recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='how_to_make',
            field=models.TextField(max_length=800, verbose_name='How To Make'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=500, validators=[recipes_app.recipes.validators.validate_ingredients], verbose_name='Ingredients'),
        ),
    ]
