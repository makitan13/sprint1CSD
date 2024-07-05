# Generated by Django 5.0.6 on 2024-07-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0020_rename_password_librarian_password1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='librarian',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]