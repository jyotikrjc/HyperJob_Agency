from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Resume
from .form import ResumeForm
# Create your views here.


def resumes(request, *args, **kwargs):
    context = {"resumes": Resume.objects.all()}
    return render(request, "resumes.html", context=context)


def new(request):
    if request.method == 'POST':
        if not request.user.is_authenticated or request.user.is_staff:
            raise PermissionDenied
        else:
            form = ResumeForm(data=request.POST)
            if form.is_valid():
                resume = request.POST.get('description')
                Resume.objects.create(description=resume, author=request.user)
                return redirect('/home')
    else:
        form = ResumeForm()
    return render(request, 'new_resume.html', {'form': form})
