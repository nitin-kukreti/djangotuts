from django.db import models

# Create your models here.
class Class(models.Model):
    name=models.CharField(max_length=16)
    def __str__(self) :
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    standerd=models.CharField(max_length=2)
    percentage=models.CharField(max_length=5)
    height=models.FloatField(max_length=12)
    classname=models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

'''
Student                                                             
     pk   name    standerd    percentage  height   classname
      1   nitin     12           80         5.10      1
class
     pk    name
      1      1st class
'''