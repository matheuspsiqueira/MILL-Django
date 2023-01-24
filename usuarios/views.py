from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from produtos.models import Produto


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        if campo_vazio(usuario) or campo_vazio(senha):
            messages.error(request, 'Por favor, preencha os campos corretamente')
            return redirect('login')

        if User.objects.filter(usuario=usuario).exists():
            nome = User.objects.filter(usuario=usuario).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('estoque')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def estoque(request):
    if request.user.is_authenticated:
        id = request.user.id
        produto = Produto.objects.order_by('-date_produto').filter(pessoa=id)
        dados={
            'produtos' : produtos
        }
        return render(request, 'estoque.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.stip()

def senha_diferente(senha, senha2):
    return senha != senha2

