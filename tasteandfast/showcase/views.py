from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [{'title': 'Taste and Fast', 'url_name': 'home'},
        {'title': 'Блюда', 'url_name': 'dishes'},
        {'title': 'Разделы меню', 'url_name': 'rubric'}]


def index(request):
    context = {'menu': menu}
    return render(request, "index.html", context=context)


def rubric(request, rubric_id):
    context = {'menu': menu}
    return render(request, "rubrics.html", context=context)


def rubrics(request):
    context = {'menu': menu}
    return render(request, "rubrics.html", context=context)


def dishes(request):
    rubrics = Rubrics.objects.all()
    context = {'menu': menu, "cats": rubrics}
    return render(request, 'dishes.html', context=context)


def show_dish(request, dish_id):
    rubrics = Rubrics.objects.all()
    context = {'menu': menu, "cats": rubrics}
    return render(request, 'dishes.html', context=context)