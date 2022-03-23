from django.db import models

# Create your models here.

class client(models.Model):
    email = models.EmailField(max_length=100, null=True)
    commentaire = models.CharField(max_length=1000)
