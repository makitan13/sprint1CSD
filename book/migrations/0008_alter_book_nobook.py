# Generated by Django 5.0.6 on 2024-06-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_nobook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='noBook',
            field=models.IntegerField(),
        ),
    ]