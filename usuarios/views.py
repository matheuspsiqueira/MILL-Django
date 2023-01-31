from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from usuarios.models import Usuario


def index(request):
    return render(request, 'index.html')

def cadastrar_funcionario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        nivel = request.POST['nivel']

        if campo_vazio(nome):
            messages.error(request, 'Nome não pode ficar em branco')
            return redirect('cadastro_funcionario')
        
        if campo_vazio(email):
            messages.error(request, 'Email não pode ficar em branco')
            return redirect('cadastro_funcionario')

        if senha_diferente(senha, senha2):
            messages.error(request, 'As senhas devem ser iguais')
            return redirect('cadastro_funcionario')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro_funcionario')
        
        if Usuario.objects.filter(nome_usuario=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro_funcionario')
        
        if nivel == 'vendedor':
            user = Usuario.objects.create(nome_usuario=nome, email=email, senha=senha, nivel=nivel)
            user.save()
            return redirect('dashboard')

        if nivel == 'coordenador':
            user = Usuario.objects.create(nome_usuario=nome, email=email, senha=senha, nivel=nivel)
            user.save()
            return redirect('dashboard')

        if nivel == 'gerente':
            user = Usuario.objects.create(nome_usuario=nome, email=email, senha=senha, nivel=nivel)
            user.save()
            return redirect('dashboard')
        
        if nivel == 'vazio':
            messages.error(request, 'Selecione um cargo válido')
            return redirect('cadastro_funcionario')
    
    else:
        return render(request, 'cadastro_funcionario.html')         

def login(request):
    if request.method == 'POST':
        nome = request.POST['username']
        senha = request.POST['senha']

        if campo_vazio(nome) or campo_vazio(senha):
            messages.error(request, 'Por favor, preencha os campos corretamente')
            return redirect('login')

        if User.objects.filter(username=nome).exists():
            nome = User.objects.filter(username=nome).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Usuário Inválido')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def senha_diferente(senha, senha2):
    return senha != senha2
