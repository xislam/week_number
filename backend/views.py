from django.shortcuts import render
import datetime

from backend.forms import DateForm


def response_date(request, *args, **kwargs):
    if request.method == 'GET':
        form = DateForm()
        return render(request, 'index.html', context={'form': form})
    elif request.method == 'POST':
        form = DateForm(data=request.POST)
        if form.is_valid():
            response = form.cleaned_data['date'].isocalendar()[1]
            context = {
                'form': form,
                'week_number': response
            }
            return render(request, 'index.html', context)

