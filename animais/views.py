
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import AnimalForm
from .models import Animal
from adocoes.models import Adocao
from historico_veterinario.models import HistoricoVeterinario


def dashboard(request):
    contexto = {
        "total_animais": Animal.objects.count(),
        "total_adocoes": Adocao.objects.count(),
        "total_historicos": HistoricoVeterinario.objects.count(),
        "animais_recentes": Animal.objects.order_by("-id")[:5],
    }

    return render(request, "dashboard.html", contexto)

def lista_animais(request):
    animais = Animal.objects.all().order_by("nome")

    return render(request, "animais/lista.html", {
        "animais": animais
    })
    

def novo_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Animal cadastrado com sucesso!")
            return redirect("lista_animais")
    else:
        form = AnimalForm()

    return render(request, "animais/form.html", {
        "form": form
    })
def detalhes_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    return render(request, "animais/detalhes.html", {
        "animal": animal
    })


def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)

        if form.is_valid():
            form.save()
            messages.success(request, "Animal atualizado com sucesso!")
            return redirect("lista_animais")
    else:
        form = AnimalForm(instance=animal)

    return render(request, "animais/form.html", {
        "form": form,
        "animal": animal
    })


def excluir_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        nome = animal.nome
        animal.delete()
        messages.success(request, f"Animal {nome} excluído com sucesso!")
        return redirect("lista_animais")

    return render(request, "animais/confirmar_exclusao.html", {
        "animal": animal
    })