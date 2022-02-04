from django import forms


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget, label="Выберите дату")

    class Meta:
        fields = ['date']

