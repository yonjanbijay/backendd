from django.db import models


class motorcycle(models.Model):
    motorcycle_model = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.motorcycle_model


class motorcycleParts(models.Model):
    partName = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/parts/', default="")

    def __str__(self):
        return self.partName
