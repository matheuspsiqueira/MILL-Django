from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from produtos.models import Produto


def index(request):
    return render(request, 'index.html')

def cadastrar_funcionario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if campo_vazio(nome):
            messages.error(request, 'Nome não pode ficar em branco')
            return redirect('cadastro_funcionario')
        
        if campo_vazio(email):
            messages.error(request, 'Email não pode ficar em branco')
            return redirect('cadastro_funcionario')

        if senha_diferente(senha, senha2):
            messages.error(request, 'As senhas devem ser iguais')
            return redirect('cadastro_funcionario')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro_funcionario')
        
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro_funcionario')
        


        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('dashboard')
    
    else:
        return render(request, 'cadastro_funcionario.html')
            

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        if campo_vazio(username) or campo_vazio(senha):
            messages.error(request, 'Por favor, preencha os campos corretamente')
            return redirect('login')

        if User.objects.filter(username=username).exists():
            nome = User.objects.filter(username=username).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('estoque')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def estoque(request):
    if request.user.is_authenticated:
        id = request.user.id
        produtos = Produto.objects.order_by('-date_produto').filter(pessoa=id)
        dados={
            'produtos' : produtos
        }
        if User.is_authenticated:
            return render(request, 'estoque.html', dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def senha_diferente(senha, senha2):
    return senha != senha2
