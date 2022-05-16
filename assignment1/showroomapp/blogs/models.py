from django.db import models

# Create your models here.
class blogspost(models.Model):
    name=models.TextField()
    username=models.TextField()
    password=models.TextField()
    phoneno=models.TextField()
