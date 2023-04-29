from django.shortcuts import render
from .models import User, Chat
from django.shortcuts import render

def index(request):
    objetos = User.objects.all()
    context = {'objetos': objetos}
    return render(request, 'Usuarios/index.html', context)
