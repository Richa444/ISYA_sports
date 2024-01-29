from django.db import models


# Create your models here.
class Volunteer(models.Model):
    """
    Model representing a contact.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone= models.CharField(max_length=50)
    message = models.TextField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
