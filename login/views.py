from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .form import UsuarioForm
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Pessoa

class UsuariosCreate(CreateView):
    template_name= "cadastros/criar.html"
    form_class= UsuarioForm
    success_url = reverse_lazy("login")
    
    def form_valid(self, form):
        
        grupo = get_object_or_404(Group, name="Docente")

        url = super().form_valid(form)
        Pessoa.objects.create(usuario=self.object)
        self.object.groups.add(grupo)
        self.object.save()

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Criar Usuario"
        context['botao'] = "Salvar"
        return context

class PessoasUpdate(UpdateView):
    template_name = "cadastros/criar.html"
    model = Pessoa
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('login')

    def get_object(self, queryset= None):
        self.object = get_object_or_404(Pessoa, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Meu dados"
        context['botao'] = "atualizar"

        return context