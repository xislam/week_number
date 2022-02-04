from django.shortcuts import render
import datetime

from backend.forms import DateForm

"""Приедстовления для определения номера недели"""


def response_date(request, *args, **kwargs):
    if request.method == 'GET':  # если запрос гет до топравь форму
        form = DateForm()
        return render(request, 'index.html', context={'form': form})
    elif request.method == 'POST':  # если запрос POST
        form = DateForm(data=request.POST)  # получаем data из requesta
        if form.is_valid():  # проверка на волидность
            response = form.cleaned_data['date'].isocalendar()[1]  # определяем номер недели
            context = {
                'form': form,
                'week_number': response
            }
            return render(request, 'index.html', context)  # Вернули результат
