from math import sqrt

from django.shortcuts import render

from .forms import triangle_form


def triangle_calculate(request):
    hypotenuse = None
    if request.method == "GET":
        t_form = triangle_form(request.POST)
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
