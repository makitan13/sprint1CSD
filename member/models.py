from django.db import models

# Create your models here.

class Member(models.Model):
    full_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
            return self.full_name    
    
    class Meta:
        db_table = 'member'
