# Generated by Django 5.0.6 on 2024-07-04 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0024_alter_librarian_managers_remove_librarian_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
