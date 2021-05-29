from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    standerd=models.CharField(max_length=2)
    percentage=models.CharField(max_length=5)
    height=models.FloatField(max_length=12)

    def __str__(self):
        return self.name

'''
Student
     pk   name    standerd    percentage  height
      1   nitin     12           80         5.10


'''