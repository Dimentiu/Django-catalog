
from math import sqrt

from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonModelForm, triangle_form
from .models import Person


def triangle_calculate(request):
    hypotenuse = None
    if request.method == "GET":
        t_form = triangle_form(request.get)
        if t_form.is_valid():
            a = t_form.cleaned_data['leg_1']
            b = t_form.cleaned_data['leg_2']
            hypotenuse = sqrt(a**2+b**2)
    else:
        t_form = triangle_form()
    return render(request,
                  "catakog/index.html",
                  {
                      'hypotenuse': hypotenuse,
                      "t_form": t_form,
                  })


def base(request):
    return render(request, 'catalog/base.html')


def select(request):
    users = Person.objects.all()
    return render(request, 'catalog/select.html', {'users': users, })


def new_person(request):
    if request.method == 'POST':
        person_form = PersonModelForm(request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('catakog:base')
    else:
        person_form = PersonModelForm()
    return render(
        request,
        'catalog/new_person.html',
        {
            'person_form': person_form,
        }
    )


def update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person_form = PersonModelForm(request.POST, instance=person)
        if person_form.is_valid():
            person_form.save()
            return redirect('catalog:base')
    else:
        person_form = PersonModelForm(instance=person)
    return render(
        request,
        'catalog/update.html',
        {
            'person_form': person_form,
            'person': person,
        }
    )
