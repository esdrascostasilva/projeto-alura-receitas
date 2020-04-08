from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Receita

# Create your views here.
def index(request):

    receitas = Receita.objects.all()
    
    dados = {
        'receitas' : receitas
    }
    
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    # a linha debaixo ele retorna o Obj e se não encontrar ele devolve o erro 404
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request, 'receita.html', receita_a_exibir)
