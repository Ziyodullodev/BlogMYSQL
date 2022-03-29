from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateTimeField(auto_now_add=True)
    mavzu = models.CharField(max_length=50)
    matn = models.TextField()
    muallif = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.mavzu}"

