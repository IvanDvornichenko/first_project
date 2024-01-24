import os
from datetime import datetime
from typing import List, Any

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime("%H:%M")
    msg = f'Текущее время: {current_time}'
    return HttpResponse("<br/>".join([
        f"<a href= '{reverse('home')}'>Возврат на главную страницу</a>",
        f"<a></a>",
        msg
    ]))


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    directory = os.getcwd()
    files = []
    files += os.listdir(directory)
    return HttpResponse("<br/>".join([
        f"<a href= '{reverse('home')}'>Возврат на главную страницу</a>",
        f"<a></a>",
        f"{' '.join(files)}"
    ]))
