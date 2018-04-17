from django.shortcuts import render


def produto_exibir(request):
    return render(request, 'produtos/produto_exibir.html', {})
