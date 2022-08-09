from django.db import models

# Create your models here.


class Item(models.Model):
    name=models.CharField(max_length=100)
    memo=models.TextField()
    stock=models.IntegerField()


    def __str__(self):
        return self.name