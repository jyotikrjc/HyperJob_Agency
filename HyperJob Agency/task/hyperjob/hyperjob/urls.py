
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from .views import signup_view, login_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='menu.html')),
    path('home', home_view),
    path('resumes/', include('resume.urls')),
    path('vacancies/', include('vacancy.urls')),
    path('resume/', include('resume.urls')),
    path('vacancy/', include('vacancy.urls')),
    path('signup', signup_view),
    path('login', login_view)
]
