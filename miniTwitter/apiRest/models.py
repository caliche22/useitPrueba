from django.db import models


class Usuario(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    alias=models.CharField(max_length=20)
    #foto=models.ImageField() Sale un error a la hora de subir una foto "post"

    def __str__(self):    ## problema de devolver la tupla
        return (self.name)
    def __str__2(self):
        return(self.email)
    def __str__3(self):
        return(self.alias)

class Post (models.Model):
    text=models.CharField(max_length=240)

    def __str__(self):
        return (self.text)

# Create your models here.