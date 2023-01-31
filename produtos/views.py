from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from produtos.models import Produto
from django.contrib.auth.models import User


def estoque(request):
    if request.user.is_authenticated:
        produtos = Produto.objects.order_by('codigo_produto')
        dados={
            'produtos' : produtos
        }
        if User.is_authenticated:
            return render(request, 'estoque.html', dados)
    else:
        return redirect('index')

def cadastra_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST['nome_produto']
        codigo_produto = request.POST['codigo_produto']
        quantidade_produto = request.POST['quantidade_produto']
        nome_fornecedor = request.POST['nome_fornecedor']
        valor_unitario = request.POST['valor_unitario']
        user = get_object_or_404(User, pk=request.user.id)
        produto = Produto.objects.create(usuario=user, nome_produto=nome_produto, codigo_produto=codigo_produto, quantidade_produto=quantidade_produto, nome_fornecedor=nome_fornecedor, valor_unitario=valor_unitario)
        produto.save()
        return redirect('estoque')
    else:
        return render(request, 'cadastra_produto.html')

def deleta_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect('estoque')

def edita_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto_a_editar = { 'produto' : produto }
    return render(request, 'edita_produto.html', produto_a_editar)

def atualiza_produto(request):
    if request.method == 'POST':
        produto_id = request.POST['produto_id']
        p = Produto.objects.get(pk=produto_id)
        p.nome_produto = request.POST['nome_produto']
        p.codigo_produto = request.POST['codigo_produto']
        p.quantidade_produto = request.POST['quantidade_produto']
        p.nome_fornecedor = request.POST['nome_fornecedor']
        p.valor_unitario = request.POST['valor_unitario']
        p.save()
        return redirect('estoque')