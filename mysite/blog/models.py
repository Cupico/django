from django.db import models

# Create your models here.
class Oiseau(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
