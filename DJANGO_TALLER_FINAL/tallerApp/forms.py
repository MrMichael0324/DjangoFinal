# from django import forms

# class InscripcionForm(forms.Form):
#     ESTADO_CHOICES = (
#         ('RESERVADO', 'Reservado'),
#         ('COMPLETADA', 'Completada'),
#         ('ANULADA', 'Anulada'),
#         ('NO ASISTEN', 'No asisten'),
#     )

#     estado = forms.ChoiceField(choices=ESTADO_CHOICES)
#     nombre = forms.CharField(max_length=50)
#     telefono = forms.IntegerField()
#     fecha_inscripcion = forms.DateField()
#     institucion = forms.CharField(max_length=50)
#     observaciones = forms.CharField(widget=forms.Textarea, required=False)