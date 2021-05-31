from django.db import models

# Create your models here.
class Car(models.Model):
    carimage=models.ImageField(upload_to="carsimages")
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