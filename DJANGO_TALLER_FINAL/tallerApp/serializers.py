from rest_framework import serializers
from .models import Inscripcion

class InscripcionSerializer(serializers.ModelSerializer):
    estado = serializers.ChoiceField(choices=Inscripcion.ESTADO_CHOICES)
    hora_inscripcion = serializers.ReadOnlyField()

    class Meta:
        model = Inscripcion
        fields = '__all__'