from django.db import models

# Create your models here.


class form_data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    message = models.TextField()
    class_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name