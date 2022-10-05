from django.db import models

# Create your models here.
class Subfamilia(models.Model):
     apellidos = models.CharField(max_length=30)
     asignacion = models.CharField(max_length=50)
     invitados = models.IntegerField()
     fecha_pago = models.DateField()