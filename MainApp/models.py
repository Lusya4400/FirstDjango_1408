from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=32)

    def __repr__(self):
        return f'Color({self.name})'

# Create your models here.
class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    descript = models.CharField(max_length=200)
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        return f'Item({self.name}, {self.brand}, {self.count})' 
