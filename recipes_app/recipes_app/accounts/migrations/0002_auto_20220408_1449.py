# Generated by Django 3.2.12 on 2022-04-08 11:49

from django.db import migrations, models
import recipes_app.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[recipes_app.accounts.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[recipes_app.accounts.validators.validate_only_letters]),
        ),
    ]
