from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import  edit, UpdateView, DeleteView, ListView, DetailView

from .models import Campo, Atividade, Aluno

# Create your views here.

class CampoCreate(edit.CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/criar.html'
    # def get_success_url(self):
    #    pk = self.kwargs["pk"]
    #    return reverse_lazy("index-cadastros")
    success_url = '/cadastros' # reverse_lazy('cadastros:index-cadastros')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campos"
        context['botao'] = "Salvar"
        return context


class AtividadeCreate(edit.CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'detalhes', 'campo', 'usuario', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('index-cadastros')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Atividades"
        context['botao'] = "Salvar"
        return context


class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/criar.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Atualização de Campos"
        context['botao'] = "Atualizar"
        return context


class AtividadeUpdate(edit.CreateView):
    model = Atividade
    fields = ['numero', 'descricao']
    template_name = 'cadastros/criar.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Atualizarção de Atividades"
        return context


class CampoDelete(DeleteView):
    model = Campo
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("index")


class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return

class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listacampos.html'
    paginate_by = 25

class AtividadeList(DetailView):
    model = Atividade
    template_name = 'cadastros/listacampos.html'
    paginate_by = 25

    def get_queryset(self):
        self.object_list = Aluno.objects.filter(usuario=self.request.user)
        return self.object_list

