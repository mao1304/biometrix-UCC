from rest_framework import serializers
from .models import Curso,Programa,Aula,Clase


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields= '__all__'
        
class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields= '__all__'
        
class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields= '__all__'
        
class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields= '__all__'