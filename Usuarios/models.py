from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class Usuario(AbstractUser):
    username = None # Remueve el campo nombre de usuario ya que usaré email como pk
    email = models.EmailField(unique=True, null=True, db_index=True, primary_key=True, max_length=50)
    avatar = models.ImageField(upload_to='core/', null=True, blank=True)

    REQUIRED_FIELDS = [] # Dentro van los campos requeridos para el registro de un nuevo usuario
    USERNAME_FIELD = 'email' # Identifica al usuario durante la autenticacion

    class Meta:
        db_table = 'Usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.CharField()

    class Meta:
        db_table = 'Mensaje'
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

