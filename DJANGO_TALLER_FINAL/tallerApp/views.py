from django.shortcuts import render
from rest_framework import generics
from .models import Inscripcion
from .serializers import InscripcionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def nombre(request):
    return render(request, 'nombre.html')

class InscripcionesClassGetPost(generics.ListCreateAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class InscripcionesClassEditDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

def lista_SN(request):
    Inscripciones=Inscripcion.objects.all()
    data={'Inscripcion':list(Inscripciones.values('id','nombre','telefono','fecha_inscripcion','institucion','estado','hora_inscripcion','observaciones'))}
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def inscripcion_list(request):
    if request.method == 'GET':
        inscripciones = Inscripcion.objects.all()
        serializer = InscripcionSerializer(inscripciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def inscripcion_detail(request, pk):
    try:
        inscripcion = Inscripcion.objects.get(pk=pk)
    except Inscripcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InscripcionSerializer(inscripcion)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = InscripcionSerializer(inscripcion, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inscripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
