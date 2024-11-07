from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name