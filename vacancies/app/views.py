from django.shortcuts import render, redirect
from .models import Vacancy, Direction
from .forms import VacancyForm, DirectionFrom
# Create your views here.


def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    directions = Direction.objects.all()
    context = {
        "vacancies": vacancies,
        "directions": directions,
    }
    return render(request, 'app/index.html', context=context)


def vacancies_by_direction(request, direction_id):
    vacancies = Vacancy.objects.filter(direction_id=direction_id)
    directions = Direction.objects.all()
    context = {
        "vacancies": vacancies,
        "directions": directions,
    }
    return render(request, 'app/index.html', context=context)


def vacancy_create(request):
    form = VacancyForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    form = VacancyForm()
    context = {
        "form": form
    }

    return render(request, 'app/vacancy_form.html', context=context)


def vacancy_detail(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)
    context = {
        "vacancy": vacancy
    }
    return render(request, 'app/vacancy_detail.html', context=context)


def vacancy_update(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)

    form = VacancyForm(data=request.POST or None, instance=vacancy)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'app/vacancy_form.html', {"form": form})


def vacancy_delete(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)

    if request.method == 'POST':
        vacancy.delete()
        return redirect('index')

    return render(request, 'app/vacancy_delete.html', {"vacancy": vacancy})


def all_directions(request):
    directions = Direction.objects.all()
    context = {
        "directions": directions,
    }

    return render(request, 'app/directions.html', context=context)


def direction_create(request):
    form = DirectionFrom(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('all_directions')

    form = DirectionFrom()
    context = {
        "form": form
    }

    return render(request, 'app/direction_form.html', context=context)


def direction_delete(request, pk):
    direction = Direction.objects.get(pk=pk)

    if request.method == 'POST':
        direction.delete()
        return redirect('all_directions')

    return render(request, 'app/direction_delete.html', {"direction": direction})


def direction_update(request, pk):
    direction = Direction.objects.get(pk=pk)

    form = DirectionFrom(data=request.POST or None, instance=direction)
    if form.is_valid():
        form.save()
        return redirect('all_directions')
    return render(request, 'app/direction_form.html', {"form": form})
