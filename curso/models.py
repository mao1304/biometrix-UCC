from django.db import models
from usuario.models import NewUser

class Programa(models.Model):
    idprograma = models.IntegerField(primary_key=True)
    info_programa = models.TextField()
    facultad = models.CharField(max_length=45)
    jefe_programa = models.CharField(max_length=45, null=True)

class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    num_clases_rest = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    ciclo = models.CharField(max_length=45)
    programa = models.ForeignKey(Programa, on_delete=models.DO_NOTHING)
    grupo = models.CharField(max_length=45)

class Aula(models.Model):
    idaula = models.IntegerField(primary_key=True)
    numero = models.IntegerField()

class Clase(models.Model):
    hora_fin = models.DateTimeField()
    hora_inicio = models.DateTimeField()
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    aula = models.ForeignKey(Aula, on_delete=models.DO_NOTHING)
    tema = models.CharField(max_length=45)
    profesor_ID = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING)

