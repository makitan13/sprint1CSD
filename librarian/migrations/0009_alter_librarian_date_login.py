# Generated by Django 5.0.6 on 2024-06-27 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0008_alter_librarian_date_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='date_login',
            field=models.DateTimeField(auto_created=datetime.datetime(2024, 6, 27, 3, 55, 43, 565767, tzinfo=datetime.timezone.utc)),
        ),
    ]
