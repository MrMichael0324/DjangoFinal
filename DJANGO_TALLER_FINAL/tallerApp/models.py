from django.db import models

class Inscripcion(models.Model):
    ESTADO_CHOICES = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No asisten'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    hora_inscripcion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)