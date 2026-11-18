
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Adocao
from .forms import AdocaoForm


def lista_adocoes(request):
    adocoes = Adocao.objects.select_related(
        "animal"
    ).all().order_by("-data_solicitacao")

    return render(request, "adocoes/lista.html", {
        "adocoes": adocoes
    })


def nova_adocao(request):
    if request.method == "POST":
        form = AdocaoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Solicitação de adoção cadastrada com sucesso!")
            return redirect("lista_adocoes")
    else:
        form = AdocaoForm()

    return render(request, "adocoes/form.html", {
        "form": form
    })


def detalhes_adocao(request, adocao_id):
    adocao = get_object_or_404(Adocao, id=adocao_id)

    return render(request, "adocoes/detalhes.html", {
        "adocao": adocao
    })


def editar_adocao(request, adocao_id):
    adocao = get_object_or_404(Adocao, id=adocao_id)

    if request.method == "POST":
        form = AdocaoForm(request.POST, instance=adocao)

        if form.is_valid():
            form.save()
            messages.success(request, "Solicitação de adoção atualizada com sucesso!")
            return redirect("lista_adocoes")
    else:
        form = AdocaoForm(instance=adocao)

    return render(request, "adocoes/form.html", {
        "form": form,
        "adocao": adocao
    })


def excluir_adocao(request, adocao_id):
    adocao = get_object_or_404(Adocao, id=adocao_id)

    if request.method == "POST":
        adocao.delete()
        messages.success(request, "Solicitação de adoção excluída com sucesso!")
        return redirect("lista_adocoes")

    return render(request, "adocoes/confirmar_exclusao.html", {
        "adocao": adocao
    })
