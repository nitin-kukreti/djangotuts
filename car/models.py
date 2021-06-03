from django.db import models

# Create your models here.
class Color(models.Model):
    color=models.CharField(max_length=10)

    def __str__(self):
        return self.color

class Car(models.Model):
    color=models.ForeignKey(Color,on_delete=models.DO_NOTHING,null=True)
    company=models.CharField(max_length=60)
    modelno=models.CharField(max_length=30)
    engine=models.CharField(max_length=30)
    power=models.IntegerField()
    autodrive=models.BooleanField(default=False)
    nitro=models.BooleanField(default=False)
    autogear=models.BooleanField(default=False)
    millage=models.CharField(max_length=30)
    about=models.TextField()
    launchdata=models.DateTimeField(auto_now_add=True)
    price=models.FloatField(max_length=10)
    isSport=models.BooleanField(default=False)
    def __str__(self):
            return self.modelno

class Carimage(models.Model):
    carimage=models.ImageField(upload_to="carsimages") 
    car=models.ForeignKey(Car,on_delete=models.CASCADE)   

    def __str__(self):
        return self.car.modelno


