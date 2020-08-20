from django import forms


class VacancyForm(forms.Form):
    vacancy = forms.CharField(max_length=1024, label='Vacancy')
