# Generated by Django 5.0.6 on 2024-06-27 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0007_alter_librarian_date_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='date_login',
            field=models.DateTimeField(),
        ),
    ]