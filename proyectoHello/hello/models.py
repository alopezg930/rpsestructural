# from typing import Reversible
from django.db import models

# Create your models here.

class paciente(models.Model):
    
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "paciente"
        verbose_name_plural = "pacientes"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("paciente_detail", kwargs={"pk": self.pk})

class tessiu(models.Model):
    
    temperature = models.FloatField(verbose_name="temperatura")
    color = models.FloatField()
    inflammation = models.FloatField(verbose_name="inflamacion")
    name = models.ForeignKey(paciente, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "tejido"
        verbose_name_plural = "tejidos"

    def __str__(self):
        return str(self.temperature)

    # def get_absolute_url(self):
        # return Reversible("tejido_detail", kwargs={"pk": self.pk})

class distancia(models.Model):
    
    r1 = models.IntegerField(verbose_name="r1")
    r2 = models.IntegerField(verbose_name="r2")
    distancia = models.FloatField(verbose_name="distancias")    

    class Meta:
        verbose_name = "distancia"
        verbose_name_plural = "distancias"

    def __str__(self):
        return self.distancia

    # def get_absolute_url(self):
    #     return reverse("distancia_detail", kwargs={"pk": self.pk})