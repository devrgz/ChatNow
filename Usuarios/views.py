from django.shortcuts import render
from .models import User, Chat
from django.views.generic import CreateView, TemplateView

def index(request):
    objetos = User.objects.get(username="xdevrgz")
    print(objetos)
    context = {'objetos': objetos}
    return render(request, 'Usuarios/index.html', context)

class Login(TemplateView):
    template_name = 'login.html'



