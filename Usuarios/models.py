from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from .utils import get_default_image, get_user_image


# Clase que no contiene campos, si no, metodos de clase
class AccountManager(BaseUserManager):

    def create_user(self, username, email, password):
        if not username:
            raise ValueError('Es necesario ingresar un nombre de usuario')
        if not email:
            raise ValueError('Es necesario ingresar un correo electronico')
        user = self.model(
            email=self.normalize_email(email), #Normaliza las direcciones de correo electrónico reduciendo la porción de dominio de la dirección de correo electrónico.
            username=username
        )
        user.set_password(password) # Codifica la contraseña y la ingresa a una base de datos
        user.save(using=self._db) # Detecta en que base de datos se tendria que guardar, sirve en casos de 2+ db
        return user

    def create_super_user(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):

    first_name = None
    last_name = None
    username = models.CharField(primary_key=True, db_index=True, unique=True, max_length=25)
    avatar = models.ImageField(upload_to=get_user_image, default=get_default_image, null=True, blank=True) # Default, atributo que sirve para cada instancia a la cual no se le proporciona ningun valor
    hide_email = models.BooleanField(default=True)
    REQUIRED_FIELDS = ['username', 'email', 'password'] # Dentro van los campos requeridos para el registro de un nuevo usuario
    USERNAME_FIELD = 'username' # Identifica al usuario durante la autenticacion

    
    def has_perm(self):
        return self.is_admin

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Chat(models.Model):

    id = models.AutoField(primary_key=True)
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="remitente")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receptor")
    tiempo = models.DateField(default=timezone.now)
    mensaje = models.CharField(max_length=250)

    def __str__(self):
        return self.remitente, self.receptor

    class Meta:
        db_table = 'Mensaje'
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

