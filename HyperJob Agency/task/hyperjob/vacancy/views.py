from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Vacancy
from .form import VacancyForm

# Create your views here.


def vacancies(request, *args, **kwargs):
    context = {"vacancies": Vacancy.objects.all()}
    return render(request, "vacancies.html", context=context)


def new(request):
    if request.method == 'POST':
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied
        else:
            form = VacancyForm(data=request.POST)
            if form.is_valid():
                resume = request.POST.get('description')
                Vacancy.objects.create(description=resume, author=request.user)
                return redirect('/home')
    else:
        form = VacancyForm()
    return render(request, 'new_resume.html', {'form': form})
