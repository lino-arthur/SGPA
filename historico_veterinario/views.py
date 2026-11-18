
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import HistoricoVeterinario
from .forms import HistoricoVeterinarioForm


def lista_historicos(request):
    historicos = HistoricoVeterinario.objects.select_related(
        "animal"
    ).all().order_by("-data_procedimento")

    return render(request, "historico_veterinario/lista.html", {
        "historicos": historicos
    })


def novo_historico(request):
    if request.method == "POST":
        form = HistoricoVeterinarioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Histórico veterinário cadastrado com sucesso!"
            )
            return redirect("lista_historicos")
    else:
        form = HistoricoVeterinarioForm()

    return render(request, "historico_veterinario/form.html", {
        "form": form
    })


def detalhes_historico(request, historico_id):
    historico = get_object_or_404(
        HistoricoVeterinario,
        id=historico_id
    )

    return render(request, "historico_veterinario/detalhes.html", {
        "historico": historico
    })


def editar_historico(request, historico_id):
    historico = get_object_or_404(
        HistoricoVeterinario,
        id=historico_id
    )

    if request.method == "POST":
        form = HistoricoVeterinarioForm(
            request.POST,
            instance=historico
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Histórico veterinário atualizado com sucesso!"
            )
            return redirect("lista_historicos")
    else:
        form = HistoricoVeterinarioForm(instance=historico)

    return render(request, "historico_veterinario/form.html", {
        "form": form,
        "historico": historico
    })


def excluir_historico(request, historico_id):
    historico = get_object_or_404(
        HistoricoVeterinario,
        id=historico_id
    )

    if request.method == "POST":
        historico.delete()
        messages.success(
            request,
            "Histórico veterinário excluído com sucesso!"
        )
        return redirect("lista_historicos")

    return render(
        request,
        "historico_veterinario/confirmar_exclusao.html",
        {"historico": historico}
    )
