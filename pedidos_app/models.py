from django.db import models
from django.db.models import Q
from django.utils import timezone


class Cuenta(models.Model):
  usuario = models.CharField(max_length=80, unique=True)
  correo = models.CharField(max_length=120)

def __str__(self):
 return self.usuario


class Personaje(models.Model):
 raza = models.CharField(max_length=20)
 descripcion = models.CharField(max_length=200)
 nivel = models.IntegerField(validators=[])
 ban = models.BooleanField(default=False)
 creado = models.DateTimeField(default=timezone.now)

class Meta:
  constraints = [
   models.CheckConstraint(condition=Q(nivel__gte=0),name="personaje.sin.nivel.negativo")]

def __str__(self):
 return self.raza


class CuentaPersonaje(models.Model):
 cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE)
 personaje = models.ForeignKey(Personaje,on_delete=models.CASCADE)

def __str__(self):
 return f"{self.cuenta} - {self.personaje}"


class Categoria(models.Model):
 nombre = models.CharField(max_length=120)
 tipo = models.CharField(max_length=100, unique=True)

def __str__(self):
 return self.nombre


class Item(models.Model):
 personaje = models.ForeignKey(Personaje,on_delete=models.CASCADE)
 categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
 nombre = models.CharField(max_length=100)
 descripcion = models.TextField()
 nivel = models.IntegerField(default=0)
 cantidad = models.IntegerField(default=1)

class Meta:
 constraints = [models.CheckConstraint(condition=Q(nivel__gte=0),name="item.nivel.no.negativo")]

def __str__(self):
 return self.nombre