from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    documento=models.IntegerField()    
    ficha=models.IntegerField()
    photo=models.ImageField(upload_to='fotos_usuarios')

    def __str__(self):
        return self.nombre