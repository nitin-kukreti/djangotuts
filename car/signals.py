from django.db.models.signals import  pre_delete
from django.dispatch import receiver
from .models import *
import os
@receiver(pre_delete,sender=Carimage)
def onimagedelete(sender,instance,**kwarg):
    print(instance.carimage.path)
    os.remove(instance.carimage.path)




