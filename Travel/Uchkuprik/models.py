from django.db import models

# Create your models here.
class Travel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    term = models.FloatField()
    description = models.TextField(blank=True,null=True)
    klass = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()


    def __str__(self):
        return self.name



class Hotel(models.Model):
    name = models.CharField(max_length=150)
    stars = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return self.name