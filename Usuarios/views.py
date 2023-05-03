from django.shortcuts import render, redirect
from .models import User, Chat
from django.views.generic import CreateView, TemplateView

def index(request):
    objetos = User.objects.get(username="xdevrgz")
    print(objetos)
    context = {'objetos': objetos}
    return render(request, 'Usuarios/index.html', context)

class Login(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        """
        if not request.user.is_authenticated():
            return redirect('login')
        """
        if request.user is None:
            return redirect('login')
        return super(Login, self).dispatch(request, *args, **kwargs)



