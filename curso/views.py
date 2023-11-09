from rest_framework import viewsets
from curso import serializer as serializerCurso
from curso import models as ModelsCurso

class aulaView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.AulaSerializer
    queryset = ModelsCurso.Aula.objects.all()
    
class programaView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.ProgramaSerializer
    queryset = ModelsCurso.Programa.objects.all()
    
class claseView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.ClaseSerializer
    queryset = ModelsCurso.Clase.objects.all()
    
class cursoView(viewsets.ModelViewSet):
    serializer_class = serializerCurso.CursoSerializer
    queryset = ModelsCurso.Clase.objects.all()