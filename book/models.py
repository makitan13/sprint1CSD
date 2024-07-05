from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    isbn = models.CharField(max_length=15)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'

       
