from django.db import models
from django.contrib.auth.models import AbstractUser

    
class NewUser( AbstractUser):   

    huella = models.CharField(max_length=200, blank=True, )
    admin_check = models.BooleanField( default=False,)
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['']
    
    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = 'Usuario'  
        verbose_name_plural = 'Usuarios'  
   
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    
class faltas(models.Model):
    fecha = models.DateTimeField()
    ID_profesor = models.ForeignKey(NewUser, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.ID_profesor
    